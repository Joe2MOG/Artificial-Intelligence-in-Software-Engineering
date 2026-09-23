class TaskQueue {
  constructor(name) {
    this.queueName = name;
    this.tasks = [];
    this.isProcessing = false;
  }

  // Responsibility: Validate and add the task, then trigger lifecycle events
  addTask(taskFn, priority) {
    if (!this._isValidTask(taskFn)) {
      console.error('Task must be a function.');
      return;
    }

    this.tasks.push({ taskFn, priority, timestamp: Date.now() });

    // Delegate side-effects
    this._notifyIfHighPriority(priority);
    this._checkAndStartQueue();
  }

  // Responsibility: Input validation
  _isValidTask(taskFn) {
    return taskFn && typeof taskFn === 'function';
  }

  // Responsibility: Evaluate priority and handle notifications
  _notifyIfHighPriority(priority) {
    if (priority > 9) {
      // FIX: Accessing class property correctly instead of relying on broken closure
      console.warn(`High priority task added to ${this.queueName}.`);
    }
  }

  // Responsibility: Evaluate queue state and initiate processing if needed
  _checkAndStartQueue() {
    if (this.tasks.length === 1 && !this.isProcessing) {
      console.log(`Starting queue ${this.queueName}.`);
      this._startProcessing();
    }
  }

  // Responsibility: Handle the actual processing state (stubbed for now)
  _startProcessing() {
    this.isProcessing = true;
    // Processing logic would go here...
  }
}
