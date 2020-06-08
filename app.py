import os
import sys
from flask import Flask, render_template, url_for, request, abort, jsonify
from flask_migrate import Migrate
import json
from flask_cors import CORS

from .auth import AuthError, requires_auth
from .models import setup_db, Guide, Travel, db, db_drop_and_create_all


# Filters ------------------------------------------#
def format_list(selection_query):
    item_list = [item.format() for item in selection_query]
    return item_list

# Creating APP -------------------------------------#
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    migrate = Migrate(app, db)
    CORS(app)


    @app.route('/')
    @app.route('/home')
    def home():
        return render_template('home.html')

    # Guides ---------------------------------------#
    @app.route('/guides', methods=['GET'])
    @requires_auth('read:guides')
    def guides(jwt):
        guides = Guide.query.all()
        try:
            guides_list = format_list(Guide.query.all())
            return jsonify({
                'success': True,
                'guides': guides_list
                })
        except Exception:
            abort(404)

    # Create Guide
    @app.route('/guides', methods=['POST'])
    @requires_auth('create:guides')
    def create_guide(jwt):
        body = request.get_json()
        new_name = body.get('name', None)
        new_surname = body.get('surname', None)
        new_phone = body.get('phone', None)

        try:
            guide = Guide(name=new_name, surname=new_surname, phone=new_phone)
            guide.insert()

            guides_list = format_list(Guide.query.all())

            return jsonify({
                'success': True,
                'created': guide.id,
                'guides': guides_list
                })
        except Exception:
            abort(404)

    # Update Guide
    @app.route('/guides/<id>', methods=['PATCH'])
    @requires_auth('edit:guides')
    def edit_guide(jwt, id):
        body = request.get_json()
        guide = Guide.query.filter(Guide.id == id).one_or_none()
        if guide is None:
            abort(404)
        else:
            try:
                if 'name' in body:
                    guide.name = body.get('name')
                if 'surname' in body:
                    guide.surname = body.get('surname')
                if 'phone' in body:
                    guide.phone = body.get('phone')

                guide.update()
                edited_guide = Guide.query.filter(Guide.id == id).one_or_none()

                return jsonify({
                    'success': True,
                    'guides': edited_guide.format()
                })
            except Exception:
                abort(400)

    #  Delete Guide
    @app.route('/guides/<id>', methods=['DELETE'])
    @requires_auth('delete:guides')
    def delete_guide(jwt, id):
        guide = Guide.query.filter(Guide.id == id).one_or_none()
        if guide is None:
            abort(404)
        else:
            try:
                guide.delete()
                return jsonify({
                    'success': True,
                    'deleted': id,
                    })
            except Exception:
                abort(422)

    # Travels --------------------------------------#
    @app.route('/travels', methods=['GET'])
    @requires_auth('read:travels')
    def travels(jwt):
        travels = Travel.query.all()
        try:
            travels_list = format_list(Travel.query.all())
            return jsonify({
                'success': True,
                'travels': travels_list
                })
        except Exception:
            abort(404)

    # Create Travel
    @app.route('/travels', methods=['POST'])
    @requires_auth('create:travels')
    def create_travel(jwt):
        body = request.get_json()
        new_title = body.get('title', None)
        new_content = body.get('content', None)
        new_guide_id = body.get('guide_id', None)

        try:
            travel = Travel(title=new_title, content=new_content, guide_id=new_guide_id)
            travel.insert()

            travels_list = format_list(Travel.query.all())

            return jsonify({
                'success': True,
                'created': travel.id,
                'travels': travels_list
            })
        except Exception:
            abort(404)

    # Update Travel
    @app.route('/travels/<id>', methods=['PATCH'])
    @requires_auth('edit:travels')
    def edit_travel(jwt, id):
        body = request.get_json()
        travel = Travel.query.filter(Travel.id == id).one_or_none()
        if travel is None:
            abort(404)
        else:
            try:
                if 'title' in body:
                    travel.title = body.get('title')
                if 'content' in body:
                    travel.content = body.get('content')
                if 'guide_id' in body:
                    travel.guide_id = body.get('guide_id')

                travel.update()
                edited_travel = Travel.query.filter(Travel.id == id).one_or_none()

                return jsonify({
                    'success': True,
                    'travels': edited_travel.format()
                })
            except Exception:
                abort(400)

    # Delete Travel
    @app.route('/travels/<id>', methods=['DELETE'])
    @requires_auth('delete:travels')
    def delete_travel(jwt, id):
        travel = Travel.query.filter(Travel.id == id).one_or_none()
        if travel is None:
          abort(404)
        else:
            try:
                travel.delete()
                return jsonify({
                    'success': True,
                    'deleted': id,
                    })
            except Exception:
                abort(422)

    # Error Handling -------------------------------#
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(AuthError)
    def auth_error_message(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error['code']
        }), error.status_code

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
