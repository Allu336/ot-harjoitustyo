from invoke import task

@task
def start(ctx):
    ctx.run("PY src/Tetris.py")
