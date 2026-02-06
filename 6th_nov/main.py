def sentence(word):
    max_count=1
    count=1
    for i in range(0,len(word)):
        for j in range(i+1,len(word)):
            if word[i]==word[j]:
                count=count+1
        if count > max_count:
            max_count=count
        count=1    
    print(max_count)
        
sentence("success")
sentence("mississippi")
sentence("python")