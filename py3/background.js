
(function(){
    // Issue a new GET request
    function xhr(url, ifexists, ifnotexists, retry_interval) {
        var retry_time = retry_interval || 5;
        var req = new XMLHttpRequest();
        console.log("Fetching: " + url);
        req.open("GET", url);
        req.onreadystatechange=function(){
            if (req.readyState == 4){
                var status=req.status;
                if ((status == 200) || (status == 301) || (status == 302)) {
                    ifexists(url, req);
                } else {
                    ifnotexists(url, req);
                    setTimeout(function() { xhr(url, ifexists, ifnotexists, retry_time + 5).send(null); }, retry_time);
                }
            }
        };
        return req;
    };
    
    // Navigates to the specified URL.
    function nav(url) {
        console.log("Navigating to: " + url);
        chrome.tabs.getSelected(null, function(tab) {
            chrome.tabs.update(tab.id, {url: url});
        });
    };
    
    // Sets the the default styling for the first search item
    function setDefaultSuggestion(text) {
        if (text) {
            chrome.omnibox.setDefaultSuggestion({"description":"<url><match>Python3 Search</match></url> " + text});
        } else {
            chrome.omnibox.setDefaultSuggestion({"description":"<url><match>Python3 Search</match></url>"});
        }
    };

    Storage.prototype.setObject = function(key, value) {
        this.setItem(key, JSON.stringify(value));
    }
    
    Storage.prototype.getObject = function(key) {
        var value = this.getItem(key);
        return value && JSON.parse(value);
    }
    
    var builtin_functions_ = null;
    var constants_ = null;
    var types_ = null;
    var exceptions_ = null;
    var datamodel_ = null;
    var modules_ = null;
    
    chrome.omnibox.onInputStarted.addListener(function(){
        console.log("Input started");
        setDefaultSuggestion('');
        
        if (localStorage.hasOwnProperty('python_builtin_functions')) {
            builtin_functions_ = localStorage.getObject('python_builtin_functions');
        } else {
            xhr("http://docs.python.org/3/library/functions.html",
            function(url, req) {
                console.log("Received: "+url);
                builtin_functions_ = {};
                builtin_functions_["builtin functions"] = {"name":"Builtin Functions", "url":"http://docs.python.org/3/library/functions.html"};
                var text = req.responseText;
                //var matches = text.match(new RegExp("<a title=\"[^\"]*\" class=\"reference [a-z]*\" href=\"[^\"]*\"><tt class=\"xref docutils literal\"><span class=\"pre\">[^<]*</span></tt></a></td>", "g"));
                var matches = text.match(
                    new RegExp('<a class=\"[^\"]*\" href=\"[^\"]*\" title=\"[^\"]*"><code class=\"xref py py-func docutils literal notranslate\"><span class=\"pre\">[^<]*<\/span><\/code><\/a>', "g"));
                console.log(text.substr(100, 200), "**Matches**", matches); 
                if (matches) {
                    for (var i = 0; i < matches.length; ++i) {
                        var match = matches[i];
                        var hrefstartidx = match.indexOf("href=\"") + 6;
                        var hrefendidx = match.indexOf("\"", hrefstartidx);
                        var href = match.substring(hrefstartidx, hrefendidx);
                        var hashidx = href.indexOf("#");
                        var name = href.substr(hashidx+1);
                        var url = (hashidx == 0) ? ("http://docs.python.org/3/library/functions.html" + href) : ("http://docs.python.org/3/library/" + href);
                        builtin_functions_[name.toLowerCase()] = {"name":name, "url":url};
                    }
                    console.log("BUILT-IN", builtin_functions_);
                    localStorage.setObject('python_builtin_functions', builtin_functions_);
                }
            },
            function (url, req) {
                console.log("Failed to receive: "+url);
            }).send(null);
        }
        
        if (localStorage.hasOwnProperty('python_constants')) {
            constants_ = localStorage.getObject('python_constants');
        } else {
            xhr("http://docs.python.org/3/library/constants.html",
            function(url, req) {
                console.log("Received: "+url);
                constants_ = {};
                constants_["constants"] = {"name":"Constants", "url":"http://docs.python.org/3/library/constants.html"};
                var text = req.responseText;
                var matches = text.match(new RegExp("<a class=\"headerlink\" href=\"#[^\"]*\" title=\"Permalink to this definition\">[^\"]*</a>", "g"));
                for (var i = 0; i < matches.length; ++i) {
                    var match = matches[i];
                    var hrefstartidx = match.indexOf("href=\"") + 6;
                    var hrefendidx = match.indexOf("\"", hrefstartidx);
                    var href = match.substring(hrefstartidx, hrefendidx);
                    var name = href.substr(1);
                    constants_[name.toLowerCase()] = {"name":name, "url":url + href};
                }
                localStorage.setObject('python_constants', constants_);
            },
            function (url, req) {
                console.log("Failed to receive: "+url);
            }).send(null);
        }
        
        if (localStorage.hasOwnProperty('python_types')) {
            types_ = localStorage.getObject('python_types');
        } else {
            xhr("http://docs.python.org/3/library/stdtypes.html",
            function(url, req) {
                console.log("Received: "+url);
                types_ = {};
                types_["types"] = {"name":"Types", "url":"http://docs.python.org/3/library/stdtypes.html"};
                var text = req.responseText;
                var matches = text.match(new RegExp("<a class=\"headerlink\" href=\"#[^\"]*\" title=\"Permalink to this definition\">[^\"]*</a>", "g"));
                for (var i = 0; i < matches.length; ++i) {
                    var match = matches[i];
                    var hrefstartidx = match.indexOf("href=\"") + 6;
                    var hrefendidx = match.indexOf("\"", hrefstartidx);
                    var href = match.substring(hrefstartidx, hrefendidx);
                    var name = href.substr(1);
                    types_[name.toLowerCase()] = {"name":name, "url":url + href};
                }
                localStorage.setObject('python_types', types_);
            },
            function (url, req) {
                console.log("Failed to receive: "+url);
            }).send(null);
        }
        
        if (localStorage.hasOwnProperty('python_exceptions')) {
            exceptions_ = localStorage.getObject('python_exceptions');
        } else {
            xhr("http://docs.python.org/3/library/exceptions.html",
            function(url, req) {
                console.log("Received: "+url);
                exceptions_ = {};
                exceptions_["exceptions"] = {"name":"exceptions", "url":"http://docs.python.org/3/library/exceptions.html"};
                var text = req.responseText;
                var matches = text.match(new RegExp("<a class=\"headerlink\" href=\"#[^\"]*\" title=\"Permalink to this definition\">[^\"]*</a>", "g"));
                for (var i = 0; i < matches.length; ++i) {
                    var match = matches[i];
                    var hrefstartidx = match.indexOf("href=\"") + 6;
                    var hrefendidx = match.indexOf("\"", hrefstartidx);
                    var href = match.substring(hrefstartidx, hrefendidx);
                    var name = href.substr(1);
                    exceptions_[name.toLowerCase()] = {"name":name, "url":url + href};
                    var exceptions_dot_index = name.indexOf("exceptions.");
                    if (exceptions_dot_index == 0) {
                        var shortname = name.substr(11);
                        types_[shortname.toLowerCase()] = {"name":shortname, "url":url + href};
                    }
                }
                localStorage.setObject('python_exceptions', exceptions_);
            },
            function(url, req) {
                console.log("Failed to receive: "+url);
            }).send(null);
        }
        
        if (localStorage.hasOwnProperty('python_datamodel')) {
            datamodel_ = localStorage.getObject('python_datamodel');
        } else {
            xhr("http://docs.python.org/3/reference/datamodel.html",
            function(url, req) {
                console.log("Received: "+url);
                datamodel_ = {};
                var text = req.responseText;
                var matches = text.match(new RegExp("<a class=\"headerlink\" href=\"#[^\"]*\" title=\"Permalink to this definition\">[^<]*</a>", "g"));
                for (var i = 0; i < matches.length; ++i) {
                    var match = matches[i];
                    var match = matches[i];
                    var hrefstartidx = match.indexOf("href=\"") + 6;
                    var hrefendidx = match.indexOf("\"", hrefstartidx);
                    var href = match.substring(hrefstartidx, hrefendidx);
                    var name = href.substr(1);
                    datamodel_[name.toLowerCase()] = {"name":name, "url":url + href};
                    if (name.startsWith("object.")) {
                        var shortname = name.substr(7);
                        datamodel_[shortname.toLowerCase()] = {"name":shortname, "url":url + href};
                    } else if (name.startsWith("class.")) {
                        var shortname = name.substr(6);
                        datamodel_[shortname.toLowerCase()] = {"name":shortname, "url":url + href};
                    }
                }
                localStorage.setObject('python_datamodel', datamodel_);
            },
            function(url, req) {
                console.log("Failed to receive: "+url);
            }).send(null);
        }
        
        if (localStorage.hasOwnProperty('python_modules')) {
            modules_ = localStorage.getObject('python_modules');
        } else {
            var tt_start = new RegExp("<code class=\"xref\">", "g");
            var tt_end = new RegExp("</code></a>", "g");
            var em_start = new RegExp("<em>", "g");
            var em_end = new RegExp("</em>", "g");
            var td = new RegExp("</td><td>", "g");
            var deprecated = new RegExp("<strong>Deprecated:</strong>", "g");
            xhr("http://docs.python.org/3/py-modindex.html",
            function(url, req) {
                console.log("Received: "+url);
                modules_ = {};
                var text = req.responseText;
                //var matches = text.match(new RegExp('<a href=\"library/[^\"]*.html#module-[^\"]*\"><tt class=\"xref\">[^<]*</tt></a>( <em>\\(.*\\)</em>)?</td><td>(<strong>Deprecated:</strong>)?', "g"));
                var matches = text.match(
                    new RegExp('<a href=\"library\/[^\"]*.html#module-[^\"]*\"><code class=\"xref\">[^<]*<\/code><\/a><\/td><td>\n?.*<em>[^<]*<\/em>', "g"));
                            
                if (matches) {
                    for (var i = 0; matches !== null && i < matches.length; ++i) {
                        // console.log(matches[i]);
                        var match = matches[i];
                        var hrefstartidx = match.indexOf("href=\"") + 6;
                        var hrefendidx = match.indexOf("\"", hrefstartidx);
                        var href = match.substring(hrefstartidx, hrefendidx);
                        var namestartidx = match.indexOf("\"xref\">") + 7;
                        var nameendidx = match.indexOf("</code>", namestartidx);
                        var name = match.substring(namestartidx, nameendidx);
                        var fullurl = "http://docs.python.org/3/" + href;
                        var description = [match.substr(match.indexOf("<code"))
                                                .replace(tt_start, "<match>")
                                                .replace(tt_end, "</match>")
                                                .replace(em_start, "<dim>")
                                                .replace(em_end, "</dim>")
                                                .replace(td, "")
                                                .replace(deprecated, " <match>[DEPRECATED]</match>"),
                                            " - <url>", fullurl, "</url>"].join('');
                        modules_[name.toLowerCase()] = {"name":name, "url":fullurl, "description":description};
                        console.log("***", modules_[name.toLowerCase()]);
                    }
                    localStorage.setObject('python_modules', modules_);
                }
            },
            function(url, req) {
                console.log("Failed to receive: "+url);
            }).send(null);
        }
    });
    
    function fetchModule(moduleobj) {
        console.log(moduleobj);
        if (moduleobj["moduledata"]) {
            return;
        }
        moduleobj["moduledata"] = {};
        var moduleurl = moduleobj["url"];
        var hashidx = moduleurl.indexOf("#");
        var url = (hashidx == -1) ? moduleurl : moduleurl.substring(0, hashidx);
        xhr(url,
        function(url, req) {
            console.log("Received: "+url);
            var text = req.responseText;
            var matches = text.match(new RegExp("<a class=\"headerlink\" href=\"#[^\"]*\" title=\"Permalink to this definition\">[^<]*</a>", "g"));
            if (matches) {
                for (var i = 0; matches !== null && i < matches.length; ++i) {
                    var match = matches[i];
                    var hrefstartidx = match.indexOf("href=\"") + 6;
                    var hrefendidx = match.indexOf("\"", hrefstartidx);
                    var href = match.substring(hrefstartidx, hrefendidx);
                    var name = href.substr(1);
                    moduleobj["moduledata"][name.toLowerCase()] = {"name":name, "url":url + href};
                }
            }
        },
        function(url, req) {
            console.log("Failed to receive: "+url);
        }).send(null);
    }
    
    chrome.omnibox.onInputCancelled.addListener(function() {
        console.log("Input cancelled.");
        setDefaultSuggestion('');
    });
    
    setDefaultSuggestion('');
    
    // Event handler for when user input is received.
    chrome.omnibox.onInputChanged.addListener(function(text, suggest_callback) {
        setDefaultSuggestion(text);
        // console.log("changed:", text);
        if (!text) {
            return;
        }
        
        var kMaxSuggestions = 20;
        var suggestions = [];
        var stripped_text = text.strip();
        if (!stripped_text) {
            return;
        }
        var qlower = stripped_text.toLowerCase();
        
        /*if ("print".startsWith(qlower)) {
          console.log("***print?"); 
            suggestions.push({
            "content":"http://docs.python.org/release/3.0.1/library/functions.html#print",
            "description":"<match>print<match> - <url>http://docs.python.org/release/3.0.1/library/functions.html#print</url>"});

        }*/
        
        for (var key in predefined_) {
            if (key.startsWith(qlower)) {
                var url = "http://docs.python.org/3/" + predefined_[key];
                suggestions.push({"content":url, "description":["<match>", key, "</match> - <url>", url, "</url>"].join('')});
                if (suggestions.length > kMaxSuggestions) {
                    break;
                }
            }
        }
        
        if (suggestions.length > kMaxSuggestions) {
            suggest_callback(suggestions);
            return;
        }
        
        if (datamodel_) {
            for (var key in datamodel_) {
                if (key.startsWith(qlower)) {
                    var entry = datamodel_[key];
                    var url = entry["url"];
                    var name = entry["name"];
                    suggestions.push({"content":url, "description":["<match>", name, "</match> - <url>", url, "</url>"].join('')});
                    if (suggestions.length > kMaxSuggestions) {
                        break;
                    }
                }
            }
        }
        
        if (suggestions.length > kMaxSuggestions) {
            suggest_callback(suggestions);
            return;
        }
        
        if (types_) {
            for (var key in types_) {
                if (key.startsWith(qlower)) {
                    var entry = types_[key];
                    var url = entry["url"];
                    var name = entry["name"];
                    suggestions.push({"content":url, "description":["<match>", name, "</match> - <url>", url, "</url>"].join('')});
                    if (suggestions.length > kMaxSuggestions) {
                        break;
                    }
                }
            }
        }
        
        if (suggestions.length > kMaxSuggestions) {
            suggest_callback(suggestions);
            return;
        }
        
        if (exceptions_) {
            for (var key in exceptions_) {
                if (key.startsWith(qlower)) {
                    var entry = exceptions_[key];
                    var url = entry["url"];
                    var name = entry["name"];
                    suggestions.push({"content":url, "description":["<match>", name, "</match> - <url>", url, "</url>"].join('')});
                    if (suggestions.length > kMaxSuggestions) {
                        break;
                    }
                }
            }
        }
        
        if (suggestions.length > kMaxSuggestions) {
            suggest_callback(suggestions);
            return;
        }

        //console.log(builtin_functions_);
        if (builtin_functions_) {
            for (var key in builtin_functions_) {
                if (key.startsWith(qlower)) {
                    var entry = builtin_functions_[key];
                    var url = entry["url"];
                    var name = entry["name"];
                    if (types_[key] || predefined_[key]) {
                        suggestions.push({"content":url, "description":["<match>", name, "</match> <dim>(function)</dim> - <url>", url, "</url>"].join('')});
                    } else {
                        suggestions.push({"content":url, "description":["<match>", name, "</match> - <url>", url, "</url>"].join('')});
                    }
                    if (suggestions.length > kMaxSuggestions) {
                        break;
                    }
                }
            }
        }
        
        if (suggestions.length > kMaxSuggestions) {
            suggest_callback(suggestions);
            return;
        }

        if (constants_) {
            for (var key in constants_) {
                if (key.startsWith(qlower)) {
                    var entry = constants_[key];
                    var url = entry["url"];
                    var name = entry["name"];
                    suggestions.push({"content":url, "description":["<match>", name, "</match> - <url>", url, "</url>"].join('')});
                    if (suggestions.length > kMaxSuggestions) {
                        break;
                    }
                }
            }
        }
        
        if (suggestions.length > kMaxSuggestions) {
            suggest_callback(suggestions);
            return;
        }

        if (modules_) {
            for (var key in modules_) {
                if (key.startsWith(qlower)) {
                    var entry = modules_[key];
                    fetchModule(entry);
                    var url = entry["url"];
                    var name = entry["name"];
                    suggestions.push({"content":url, "description":entry["description"]});
                    if (suggestions.length > kMaxSuggestions) {
                        break;
                    }
                }
                if (key.startsWith(qlower) || qlower.startsWith(key)) {
                    var entry = modules_[key];
                    if (entry["moduledata"]) {
                        var moduledata = entry["moduledata"];
                        for (var subkey in moduledata) {
                            if (subkey.startsWith(qlower)) {
                                var subentry = moduledata[subkey];
                                var url = subentry["url"];
                                var name = subentry["name"];
                                suggestions.push({"content":url, "description":["<match>", name, "</match> - <url>", url, "</url>"].join('')});
                                if (suggestions.length > kMaxSuggestions) {
                                    break;
                                }
                            }
                        }
                    }
                }
            }
        }
        
        if (suggestions.length > kMaxSuggestions) {
            suggest_callback(suggestions);
            return;
        }

        if (stripped_text.length >= 2) {
            suggestions.push({"content":stripped_text +  " [Google Code Search]", 
                "description":["Search for \"<match>", stripped_text, "</match> <dim>lang:python</dim>\" using <match><url>Google Code Search</url></match> - <url>http://code.google.com/codesearch#search/&amp;q=", encodeURIComponent(stripped_text + " lang:python"), "</url>"].join('')}); 
            suggestions.push({"content":stripped_text +  " [Development and Coding Search]", 
                "description":["Search for \"<match>", stripped_text, "</match>\" using <match><url>Develoment and Coding Search</url></match> - <url>http://www.google.com/cse?cx=005154715738920500810:fmizctlroiw&amp;q=", encodeURIComponent(stripped_text), "</url>"].join('')});
        }
        // console.log("changed: suggestions", suggestions);
        suggest_callback(suggestions);
    });
    
    // Event handler for when the enter key is pressed within the omnibox.
    chrome.omnibox.onInputEntered.addListener(function(text) {
        console.log("Input entered: " + text);
        if (!text) {
            nav("http://docs.python.org/3/");
            return;
        }
        
        var stripped_text = text.strip();
        if (!stripped_text) {
            nav("http://docs.python.org/3/");
            return;
        }
        var qlower = stripped_text.toLowerCase();
        
        if (stripped_text.startsWith("http://") || stripped_text.startsWith("https://")) {
            nav(stripped_text);
            return;
        }
        
        if (stripped_text.startsWith("www.") || stripped_text.endsWith(".com") || stripped_text.endsWith(".net") || stripped_text.endsWith(".org") || stripped_text.endsWith(".edu")) {
            nav("http://" + stripped_text);
            return;
        }
                
        var google_codesearch_suffix = " [Google Code Search]";
        if (stripped_text.endsWith(google_codesearch_suffix)) {
            var newquery = stripped_text.substring(0, stripped_text.length - google_codesearch_suffix.length).strip();
            nav("http://code.google.com/codesearch#search/&q=" + encodeURIComponent(newquery + " lang:python"));
            return;
        }
        
        var devsearch_suffix = " [Development and Coding Search]";
        if (stripped_text.endsWith(devsearch_suffix)) {
            var newquery = stripped_text.substring(0, stripped_text.length - devsearch_suffix.length).strip();
            nav("http://www.google.com/cse?cx=005154715738920500810:fmizctlroiw&q=" + encodeURIComponent(newquery));
            return;
        }
        
        /*console.log("qlower ", qlower);
        if (qlower == "print") {
            nav("http://docs.python.org/release/3.0.1/library/functions.html#print");
            return;
        }*/
        
        if (predefined_[qlower]) {
            nav("http://docs.python.org/3/" + predefined_[qlower]);
            return;
        }
        
        if (datamodel_ && datamodel_[qlower]) {
            nav(datamodel_[qlower]["url"]);
            return;
        }
        
        if (types_ && types_[qlower]) {
            nav(types_[qlower]["url"]);
            return;
        }
        
        if (exceptions_ && exceptions_[qlower]) {
            nav(exceptions_[qlower]["url"]);
            return;
        }
        
        if (builtin_functions_ && builtin_functions_[qlower]) {
            nav(builtin_functions_[qlower]["url"]);
            return;
        }

        if (constants_ && constants_[qlower]) {
            nav(constants_[qlower]["url"]);
            return;
        }

        if (modules_) {
            if (modules_[qlower]) {
                nav(modules_[qlower]["url"]);
                return;
            }
                
            for (var key in modules_) {
                if (qlower.startsWith(key)) {
                    var entry = modules_[key];
                    if (entry["moduledata"] && entry["moduledata"][qlower]) {
                        nav(entry["moduledata"][qlower]["url"]);
                        return;
                    }
                }
            }
        }
        
        nav("http://www.google.com/search?q=" + encodeURIComponent("Python "+stripped_text));
    });
})();