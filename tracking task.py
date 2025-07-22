#!/usr/bin/env python
# coding: utf-8

# In[8]:


import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
if not ret:
    print("The frame is not read")
    cap.release()
    exit()

bbox = cv2.selectROI("the object detection", frame, fromCenter=False, showCrosshair=True)

tracker = cv2.TrackerCSRT_create()
tracker.init(frame, bbox)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    success, bbox = tracker.update(frame)

    if success:
        x, y, w, h = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  
        cv2.putText(frame, "Target", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    else:
        cv2.putText(frame, "Lost", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("follow the object", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[10]:





# In[10]:





# In[11]:





# In[12]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




