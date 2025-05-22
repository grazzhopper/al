mod cli;
mod manager;
mod models;

use cli::interface::start_cli;
use manager::task_manager::TaskManager;

fn main() {
    let mut tm = TaskManager {
        tasks: Vec::new(),
        file_path: "tasks.json".to_string(),
    };
    start_cli(&mut tm);
}
