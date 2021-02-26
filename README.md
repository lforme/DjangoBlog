# DjangoBlog
我的博客项目

func classFromString(_ className: String) -> AnyClass? {
            let cls: AnyClass? = NSClassFromString("\(className)")
            return cls
        }
    
        guard let cls = classFromString("MercuryServiceTool") as? NSObject.Type else {
            return
        }
        
        func extractMethodFrom(owner: AnyObject, selector: Selector) -> ((String) -> AnyObject)? {
            
            let method: Method?
            if owner is AnyClass {
                method = class_getClassMethod(owner as? AnyClass, selector)!
            } else {
                method = class_getInstanceMethod(type(of: owner), selector)!
            }
            guard let m = method else {
                return nil
            }
            let implementation = method_getImplementation(m)
            typealias Function = @convention(c) (AnyObject, Selector, String) -> Unmanaged<AnyObject>
            let function = unsafeBitCast(implementation, to: Function.self)
            return { string in function(owner, selector, string).takeUnretainedValue() }
        }

        let methodName = "setupMercuryConfigWithId:"
        if let method = extractMethodFrom(owner: cls, selector: NSSelectorFromString(methodName)) {
            let appId = "80"
            _ = method(appId)
        }
