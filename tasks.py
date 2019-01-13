from celery import Celery

app = Celery("tasks",broker="redis://")

@app.task
def add(x,y): 
    return x+y

if __name__ == "__main__":
    app.worker_main()