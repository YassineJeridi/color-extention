const WorkflowIntegration = require('./WorkflowIntegration.node');
isInitialized = WorkflowIntegration.Initialize('com.blackmagicdesign.resolve.sampleplugin');


if (isInitialized) {
    resolve = WorkflowIntegration.GetResolve();
    resolve.GetProjectManager().CreateProject("Hello World");
}