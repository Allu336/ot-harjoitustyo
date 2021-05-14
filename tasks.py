from invoke import task

@task
def start(ctx):
    ctx.run("PY src/index.py")
