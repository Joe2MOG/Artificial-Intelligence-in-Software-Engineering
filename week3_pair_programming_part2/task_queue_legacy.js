class TaskQueue {
  constructor(name) {
    this.queueName = name;
    this.tasks = [];
    this.isProcessing = false;
  }

  addTask(taskFn, priority) {
    if (!taskFn || typeof taskFn !== 'function') {
      console.error('Task must be a function.');
      return;
    }

    this.tasks.push({ taskFn, priority, timestamp: Date.now() });

    if (this.tasks.length === 1) {
      console.log(`Starting queue ${this.queueName}.`);
      this._startProcessing();
    }

    function notify() {
      if (priority > 9) {
        console.warn(`High priority task added to ${name}.`);
      }
    }

    notify();
  }

  _startProcessing() {
    this.isProcessing = true;
  }
}
