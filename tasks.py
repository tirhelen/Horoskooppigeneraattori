from invoke import task

@task
def lint(ctx):
	ctx.run("pylint src")
