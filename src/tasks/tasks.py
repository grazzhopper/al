import json
import os
from pathlib import Path


class TaskManager:
    def __init__(self):
        # Use XDG data directory (~/.local/share/al/tasks.json)
        xdg_data_home = os.getenv("XDG_DATA_HOME", Path.home() / ".local" / "share")
        self.data_dir = Path(xdg_data_home) / "al"
        self.data_file = self.data_dir / "tasks.json"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.tasks = self._load_tasks()

    def _load_tasks(self):
        """Load tasks from JSON file."""
        if not self.data_file.exists():
            return []
        try:
            with self.data_file.open("r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def _save_tasks(self):
        """Save tasks to JSON file."""
        with self.data_file.open("w") as f:
            json.dump(self.tasks, f, indent=2)

    def add_task(self, description):
        """Add a new task and return its ID."""
        task_id = max((task["id"] for task in self.tasks), default=0) + 1
        self.tasks.append(
            {"id": task_id, "description": description, "completed": False}
        )
        self._save_tasks()
        return task_id

    def get_tasks(self):
        """Return all tasks."""
        return self.tasks

    def complete_task(self, task_id):
        """Mark a task as completed."""
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self._save_tasks()
                return True
        return False

    def delete_task(self, task_id):
        """Delete a task."""
        initial_len = len(self.tasks)
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        if len(self.tasks) < initial_len:
            self._save_tasks()
            return True
        return False
