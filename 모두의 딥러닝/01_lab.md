# Tensorflow 기초

1. 텐서플로우란?
2. Data Flow Graph란?
그래프 : 노드와 노드간을 엣지로 연결한 것
Data flow Graph : 엣지는 이제 데이터(tensors)라고 불러준다. 기존의 그래프 처럼 그래프 안에서 데이터들이 돌아다니는 것이다.
3. 텐서플로우 기초
- Hello Tensorflow!
    <pre><code>import tensorflow as tf
    
    hello = tf.constant("Hello, Tensorflow!")
    sess = tf.Session() # 항상 Session을 만들고 해야 한다.
    print(sess.run(hello)) #Hello, Tensorflow 출력 
    </code></pre>
    
 - Easy Graph
    <pre><code>import tensorflow as tf

    a = tf.constant(3.0, tf.float32) #데이터 타입이 float32인 노드 생성 (3)
    b = tf.constant(4.0) #4
    c = tf.mul(a, b) #a와 b를 곱해준다

    sess = tf.Session()
    print("a, node2 : " , sess.run(a, b))
    print("c : ", sess.run(c)) #12 출력
    </code></pre>

 - Placeholder
    <pre><code>import tensorflow as tf
    a = tf.placeholder(tf.float32)
    b = tf.placeholder(tf.float32)
    add = a+b

    sess = tf.Session()
    print(sess.run(add, feed_dict={a : 3.0, b : 4.0})
    print(sess.run(add, feed_dict={a:[3,9], b:[2,3]}))

    #placeholder는 데이터가 들어갈 위치만 잡아 놓는 것이다. 실제로는 feed_dict를 사용해서 데이터를 넣어주어야 한다.
    </code></pre>

