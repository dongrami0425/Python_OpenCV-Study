

import numpy as np
import tensorflow as tf


image_Path = 'firstnw/pathrecord/newimage/123.jpg'
modelFullPath = 'C:/Users/ldm81/PycharmProjects/capstoneproject/firstnw/output_graph.pb'
labelsFullPath = 'C:/Users/ldm81/PycharmProjects/capstoneproject/firstnw/output_labels.txt'


def create_graph():
    """저장된(saved) GraphDef 파일로부터 graph를 생성하고 saver를 반환한다."""
    with tf.gfile.FastGFile(modelFullPath, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')


def run_inference_on_image(imagePath):
    answer = None

    if not tf.gfile.Exists(imagePath):
        tf.logging.fatal('파일이 존재하지 않습니다: %s', imagePath)
        return answer

    image_data = tf.gfile.FastGFile(imagePath, 'rb').read()

    # 저장된(saved) GraphDef 파일로부터 graph를 생성한다.
    create_graph()

    with tf.Session() as sess:

        ## 학습이 끝난 마지막 소프트맥스 텐서를 가져온다.
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        ## 이미지 데이터를 네트워크 맨 앞에 넣어 분류를 실행한다.
        predictions = sess.run(softmax_tensor,
                               {'DecodeJpeg/contents:0': image_data})
        ## [[]]로 중첩된 어레이가 떨어지는데 np.squeeze로 하나의 어레이로 만든다.
        predictions = np.squeeze(predictions)

        ## 가장 높은 확률 값을 가진 5개를 선택한다. 여기서는 클래스가 3개 뿐이라 3개만 출력된다.
        top_k = predictions.argsort()[-5:][::-1]
        print(top_k)
        f = open(labelsFullPath, 'rb')
        lines = f.readlines()
        labels = [str(w).replace("\n", "") for w in lines]
        for node_id in top_k:
            human_string = labels[node_id]
            score = predictions[node_id]
            print('%s (score = %.5f)' % (human_string, score))

        answer = labels[top_k[0]]
        return answer

run_inference_on_image(image_Path)