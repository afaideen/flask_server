

from main import app, socketio

# app = create_app()
if __name__ == '__main__':
    # socketio.run(app, debug=False, port=5050)
    socketio.run( app, host="0.0.0.0", port=5000, ssl_context=('cert.pem', 'key.pem') )
    # socketio.run(app, host='0.0.0.0', port=5050)
    # socketio.run(app, port=5050)
    # app.run(debug=True, port=5050)
    # app.run()







