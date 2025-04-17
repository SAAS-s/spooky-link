from burp import IBurpExtender, IHttpListener

class BurpExtender(IBurpExtender, IHttpListener)
    def registerExtenderCallbacks(self, callbacks):
        self.callbacks = callbacks
        self.helpers = callbacks.getHelpers()
        callbacks.setExtensionName("Minimal Logger")
        callbacks.registerHttpListener(self)

    //
    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        if messageIsRequest:
            request = self.helpers.bytesToString(messageInfo.getRequest())
            print("[Request]:\n", request)
        else:
            response = self.helpers.bytesToString(messageInfo.getResponse())
            print("[Response]:\n", response)
