function make_bold(text){
    para = document.getElementById("results");

    if(para != null){
        words = titleCase(para.innerText).split(' ');
        //searchs = text.split(' ');
        inner = "";
        text = titleCase(text).split(' ');
        for(i=0; i < words.length;i++){
            if(text.indexOf(words[i]) != -1){
                inner += "<b> "+words[i]+" </b>";
                continue;
            }
            inner += " "+words[i]+" ";
        }
        para.innerHTML = inner;
    }
}

function titleCase(str) {
    // Step 1. Lowercase the string
    str = str.toLowerCase();
  
    
    // Step 2. Split the string into an array of strings
    str = str.split(' ');
    
    // str = "i'm a little tea pot".split(' ');
    // str = ["i'm", "a", "little", "tea", "pot"];
    
    // Step 3. Create the FOR loop
    for (var i = 0; i < str.length; i++) {
      str[i] = str[i].charAt(0).toUpperCase() + str[i].slice(1); 
    }
    
    // Step 4. Return the output
    return str.join(' ');
  }