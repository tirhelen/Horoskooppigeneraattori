from invoke import task

@task
def lint(ctx):
	ctx.run("pylint src")

@task
def test(ctx):
	ctx.run("pytest src")
