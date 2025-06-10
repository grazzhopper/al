import click

from tasks.tasks import TaskManager

# Initialize TaskManager with XDG-compliant storage
task_manager = TaskManager()


@click.group()
def cli():
    """Al: Artificial Logic - A simple task tracking CLI."""
    pass


@cli.command()
@click.argument("description")
def add(description):
    """Add a new task with DESCRIPTION."""
    task_id = task_manager.add_task(description)
    click.echo(f"Task {task_id} added: {description}")


@cli.command()
def list():
    """List all tasks."""
    tasks = task_manager.get_tasks()
    if not tasks:
        click.echo("No tasks found.")
        return
    for task in tasks:
        status = "✔" if task["completed"] else " "
        click.echo(f"[{status}] {task['id']}: {task['description']}")


@cli.command()
@click.argument("task_id", type=int)
def complete(task_id):
    """Mark task with TASK_ID as completed."""
    if task_manager.complete_task(task_id):
        click.echo(f"Task {task_id} marked as completed.")
    else:
        click.echo(f"Task {task_id} not found.")


@cli.command()
@click.argument("task_id", type=int)
def delete(task_id):
    """Delete task with TASK_ID."""
    if task_manager.delete_task(task_id):
        click.echo(f"Task {task_id} deleted.")
    else:
        click.echo(f"Task {task_id} not found.")


if __name__ == "__main__":
    cli()
