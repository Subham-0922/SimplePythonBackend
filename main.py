from flask import Flask, jsonify, request
app=Flask(__name__)
post=[]

@app.route('/post',methods=['POST'])
def createPost():
    data=request.get_json()
    username=data.get('username')
    caption=data.get('caption')
    post.append({'username':username,'caption':caption})
    return jsonify({'message':"Post is added Successfully"})
@app.route('/post')
def getPosts():
    return jsonify(post)
@app.route('/post/<post_id>', methods=['DELETE'])
def deletePost(post_id):
    post_id=int(post_id)
    if post_id<len(post):
        del post[post_id]
        return jsonify({'message':'Post deleted Successfully'})
    else:
        return jsonify({'message':'Post not Found'})

if __name__=='__main__':
    app.run();