from flask import Blueprint,render_template,request,redirect
from . import db
from .models import *

views=Blueprint('views',__name__)


@views.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        task_content=request.form['content']
        new_task=Todo(content=task_content)
        db.session.add(new_task)
        db.session.commit()
        return redirect('/')
        
        
    else:
        tasks=Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html',tasks=tasks)