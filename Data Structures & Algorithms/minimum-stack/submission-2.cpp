class MinStack {
private:
    std::stack<int>min;
    std::stack<int> main;

public:
    MinStack() 
    {
        
    }
    
    void push(int val) 
    {
        main.push(val);
        if( min.empty()|| val<=min.top())
        {
            min.push(val);
        }   
    }
    
    void pop() 
    {

        
        if(min.top()==main.top())
        {
            min.pop();
        }
        main.pop();
    }
    
    int top() 
    {
        return main.top();   
    }
    
    int getMin() 
    {
        return min.top();   
    }
};


