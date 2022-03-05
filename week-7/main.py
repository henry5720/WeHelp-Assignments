from webapp import create_app

if __name__ == '__main__':
    app = create_app('development')
    app.config['JSON_AS_ASCII'] = False
    app.run(use_reloader=True, port=3000, host='0.0.0.0')
