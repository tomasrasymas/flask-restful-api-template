from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from .model import Todo
from app import db

todo_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'user_id': fields.Integer
}

todo_list_fields = {
    'count': fields.Integer,
    'todos': fields.List(fields.Nested(todo_fields)),
}

todo_post_parser = reqparse.RequestParser()
todo_post_parser.add_argument('name', type=str, required=True, location=['json'],
                              help='name parameter is required')
todo_post_parser.add_argument('description', type=str, required=True, location=['json'],
                              help='description parameter is required')
todo_post_parser.add_argument('user_id', type=int, required=True, location=['json'],
                              help='user_id parameter is required')


class TodosResource(Resource):
    def get(self, todo_id=None):
        if todo_id:
            todo = Todo.query.filter_by(id=todo_id).first()
            return marshal(todo, todo_fields)
        else:
            args = request.args.to_dict()
            limit = args.get('limit', 0)
            offset = args.get('offset', 0)

            args.pop('limit', None)
            args.pop('offset', None)

            todo = Todo.query.filter_by(**args).order_by(Todo.id)
            if limit:
                todo = todo.limit(limit)

            if offset:
                todo = todo.offset(offset)

            todo = todo.all()

            return marshal({
                'count': len(todo),
                'todos': [marshal(t, todo_fields) for t in todo]
            }, todo_list_fields)

    @marshal_with(todo_fields)
    def post(self):
        args = todo_post_parser.parse_args()

        todo = Todo(**args)
        db.session.add(todo)
        db.session.commit()

        return todo

    @marshal_with(todo_fields)
    def put(self, todo_id=None):
        todo = Todo.query.get(todo_id)

        if 'name' in request.json:
            todo.name = request.json['name']

        if 'description' in request.json:
            todo.description = request.json['description']

        db.session.commit()
        return todo

    @marshal_with(todo_fields)
    def delete(self, todo_id=None):
        todo = Todo.query.get(todo_id)

        db.session.delete(todo)
        db.session.commit()

        return todo