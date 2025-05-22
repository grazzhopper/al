use crate::models::task::Task;

pub struct TaskManager {
    pub tasks: Vec<Task>,
    pub file_path: String,
}
