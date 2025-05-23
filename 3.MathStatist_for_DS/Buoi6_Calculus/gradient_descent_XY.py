def gradient_descent_linearXY (x,y, tolerance=10**(-30)):
    import numpy as np
    import sympy as sp
    
    m = sp.symbols('m') #to define m as a symbolic variable (theta[0] slope)
    b = sp.symbols('b') #to define b as a symbolic variable (theta[1] bias)

    theta = np.array([b,m])
    print('Theta vector =',theta)
    
    x_1 = np.c_[np.ones(x.shape[0]),x]
    #np.ones(x.shape[0]) to create an array containing only 1 digit with the len of x.shape[0]
    #np.c_ is to stack 1-D array into another 1-D or 2-D array (add the 1-digit columns to the left of x, creating x_1 matrix)
    
    y_hypo = np.dot(x_1,theta) 
    #theta = [b m] and x_1[i] = [1 xi] so np.dot(x_1,theta) = y_hypo = b + m*xi

    print('\nThe y_hypothesis = x_1.dot(theta) (first 5 lines):')
    for i in range(0,5):
        print(f'y_hypo_{i+1} = {y_hypo[i]}')

    #Create loss function = sum((y[i] - y_hypo[i])**2)
    loss = (1/(y.shape[0]))*sum((y[i] - y_hypo[i])**2 for i in range(y_hypo.shape[0]))

    df_loss_m = sp.diff(loss,m)
    print(f'\nDifferentiation of loss(m,b) respect to m = {df_loss_m}')

    df_loss_b = sp.diff(loss,b)
    print(f'\nDifferentiation of loss(m,b) respect to b = {df_loss_b}')

    #***************Gradient descent part**************************#
    b_temp = 5 #set initial bias value
    m_temp = 5 #set initial slope value
    learn_rate = 10       #set initial learning rate

    df_point_b = float(df_loss_b.subs({b:b_temp, m:m_temp}))
    df_point_m = float(df_loss_m.subs({b:b_temp, m:m_temp}))
    
    loop = 1
    while True:        
        b_new = b_temp - learn_rate*df_point_b
        m_new = m_temp - learn_rate*df_point_m
        
        if (np.abs(m_new-m_temp) <= tolerance) and (np.abs(b_new-b_temp) <= tolerance): break #if the gap between point_new and point <= tolerance, stop the loop      
        else:
            df_point_b_old = df_point_b
            df_point_m_old = df_point_m
            
            df_point_b = float(df_loss_b.subs({b:b_new, m:m_new}))
            df_point_m = float(df_loss_m.subs({b:b_new, m:m_new}))
            
            b_temp = b_new #update b_temp as b_new for next loop
            m_temp = m_new
            
            if np.sign(df_point_b) != np.sign(df_point_b_old) or np.sign(df_point_m) != np.sign(df_point_m_old):
                learn_rate = learn_rate/2
            else: pass
            #if f'(x) change sign, then reduce the lear_rate
            
            loop +=1 #count the number of loops needed to find convergence_point
            
    theta1 = m_new #slope            
    theta0 = b_new #bias
    
    print(f'\nAfter {loop} loops, theta[bias,slope] = {[theta0,theta1]}')

    return float(theta0), float(theta1)
    #sympy class return symbolic expression type value, with dtype = '0'
    # so have to convert to float before returnning for visualization or other task