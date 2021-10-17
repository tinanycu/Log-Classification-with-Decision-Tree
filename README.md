# Log-Classification-with-Decision-Tree
## Machine learning algorithm
I choose Decision Tree to train the models and I import DecisionTreeClassifier in Python. Decision Tree is one of the supervised learning algorithms. I choose this algorithm because it is an effective multiclass classifier and doesn’t require much preprocessing. Figure 1 shows the structure of tree based algorithm.

  ![image](https://user-images.githubusercontent.com/91185925/137643770-5b36df3a-6186-49a9-9987-4fa4f66e3b02.png)

  Figure 1. Tree based algorithm in R and Python

There is some important terminology of Decision Tree (figure 2). Root node is all the sample data. Decision node is a sub-node which splits into further sub-nodes. Terminal node, also called leaf node, is a node which doesn’t splits into further sub-nodes. Spitting is a process that divides a node into sub-nodes. Pruning is a process that removes sub-nodes of a node. Branch, also called sub-tree, is a sub section of the decision tree. A parent node is a node that splits into sub-nodes, while the sub-nodes are called child nodes.

I choose seven fields of the logs to train seven models. Each field corresponds to a decision tree classifier model. In other words, I fit each decision tree classifier with the data of one field and the corresponding attack types. I find that with this algorithm, the testing accuracy of the five folders in the folder Example_Test is 100%.

  ![image](https://user-images.githubusercontent.com/91185925/137643969-60d24721-0ac8-4a46-9043-67527cc25e98.png)

  Figure 2. Decision Tree Algorithm

## Selected fields
The fields I select are "destination", "type", "event", "source", "network" in packetbeat logs and "winlog", "event" in winlogbeat logs.
* For packetbeat logs
  * destination: This field includes the detailed information of the receiver of network exchanges or packets. It may contain “ip”, “port”, “packets”, “bytes”, etc.
    * ip: The ip address of the destination (IPv4 or IPv6)
    * port: The port of the destination
    * packets: Packets sent from the destination to the source
    * bytes: Bytes sent from the destination to the source
  * type: The type of transaction (e.g. HTTP, MySQL, etc) or “flow” for flows.
  * event: This field includes the context information about the logs. It may contain “duration”, “action”, “end”, “kind”, “category”, “start”, “dataset”, etc.
    * duration: The duration of the event. It is equal to event.end - event.start.
    * action: The action of the event such as “network flow”. It is usually defined by the implementer.
    * end: The date that the event ends or the activity is last observed.
    * kind: The high-level information of what type the event is. E.g. event
    * category: The second level information of what type the event is. E.g. network traffic
    * start: The date that the event starts or the activity is first observed.
    * dataset: The name of the dataset, which specifies which type of logs the event comes from
  * source: This field includes the detailed information of the source of the packet or the event. It may contain “ip”, “port”, “packets”, “bytes”, etc.
    * ip: The ip address of the source (IPv4 or IPv6)
    * port: The port of the source
    * packets: Packets sent from the source to the destination
    * bytes: Bytes sent from the source to the destination
  * network: This field is defined as the communication path of the host or network event. It may contain “bytes”, “transport”, “community_id”, “packets”, “type”
    * byte: Total bytes transferred, which is equal to source.bytes and destination.bytes.
    * transport: Keyword name of the transport layer.
    * community_id: A hash of source IP, source port, destination IP, destination port, and communication protocol.
* For winlogbeat logs
  * winlog: This field includes the fields specific to Windows Event Logs. It may contain “event_data”, “provider_guid”, “keywords”, “provider_name”, etc.
  * event: Similar to event in packetbeat logs, but this is for Windows Event Logs.
## Code and models
* train_and_test.py
  * This is the code for training the models (It also includes the code for testing).
  * How it works
    * Import the modules I need (figure 3).
      * json: Used to load the json files of logs
      * joblib: Used to store the models in files so that I can load the models from the files when testing
      * sklearn: This includes tools I need, such as Decision Tree classifier, TF-IDF vectorizer, make_pipeline
      * numpy: Used for matrix computing
      
        ![image](https://user-images.githubusercontent.com/91185925/137644419-9a91b4f5-634d-4c17-9471-72ea57e35eba.png)
      
        Figure 3. The modules I use in _0716058_project2.py
      
    * Create lists for each field of logs that I want to select to train the model and lists of corresponding attack types (figure 4).
    
      ![image](https://user-images.githubusercontent.com/91185925/137644540-64e60d63-6d83-4463-810e-e177f036c3b0.png)
    
      Figure 4. The list in which I put the training data
    
    * To distinguish two "event" fields, I create two list "X_train_event" (for packetbeat logs) and "X_Train_event2" (for winlogbeat logs).
    * Load the json files in the training folder (figure 5).
    
      ![image](https://user-images.githubusercontent.com/91185925/137644591-71246429-4861-48f2-8c14-db81be343b7f.png)
    
      Figure 5. Loading the packetbeat logs of attack 1
    
    * To append the fields of the training data, I define the functions add_X_Train_p (for packetbeat logs) and add_X_Train_w (for winlogbeat logs). Figure 6 and 7 show the functions.
    
      ![image](https://user-images.githubusercontent.com/91185925/137644637-f1af609e-99c8-4e3a-b1a1-b923c49e4608.png)

      Figure 6. add_X_train_p
    
      ![image](https://user-images.githubusercontent.com/91185925/137644650-f771e92a-6b2e-45e9-8f93-d8eedd71a513.png)

      Figure 7. add_X_train_w
    
    * Append the data of each select fields to the corresponding list (e.g. X_train_type). Figure 8 shows that I call the function add_X_train_p for the fields in packetbeat logs.
    
      ![image](https://user-images.githubusercontent.com/91185925/137644669-26993311-0f12-4bbe-9571-a56c7edfe753.png)

      Figure 8. Calling the function
    
    * Append the corresponding attack types to Y_Train (for packetbeat logs) and Y_Train2 (for winlogbeat logs). Figure 9 shows this.
    
      ![image](https://user-images.githubusercontent.com/91185925/137644702-55fe3660-4bec-426d-960f-f6ef421836db.png)

      Figure 9. Appending the attack types
    
    * Repeat steps d - g for attack 1 - 5.
    * Repeat step h for packetbeat logs and winlogbeat logs
    * Before training, I use TfidfVectorizer to convert the data to a matrix of TF-IDF features. I make a pipeline that do the vectorization first and then use the output data, which is vectorized to TF-IDF, as input of the Decision Tree classifier (figure 10).
    
      ![image](https://user-images.githubusercontent.com/91185925/137644732-6e2c8886-08a9-40d0-9032-e7469948d435.png)
    
      Figure 10. Converting the data of model1
    
    * Train the models model1-model7 using the seven selected fields and their corresponding attack types by Decision Tree algorithm (figure 11).
    
      ![image](https://user-images.githubusercontent.com/91185925/137644758-9503e888-61f7-49ac-b522-83c66248df4b.png)

      Figure 11. Training model1 using the destination field.
    
    * Note: This code also includes the testing part.
* test.py
  * This is the code for testing only
  * How it works
    * Import the modules I need (figure 12).
      * json: Used to load the json files of logs
      * joblib: Used to store the models in files so that I can load the models from the files when testing
      * numpy: Used for matrix computing
      * os: I use os.listdir to get the folders in the folder in the alphabetical order
      
        ![image](https://user-images.githubusercontent.com/91185925/137644825-53ee459d-3896-418c-9162-bf9275834f6f.png)
      
        Figure 12. The modules I use in _0716058_project2_test.py
      
    * Let the user input the folder name (figure 13).
    
      ![image](https://user-images.githubusercontent.com/91185925/137644874-684ce673-5804-4f6b-962b-f079ff8a2dc0.png)

      Figure 13. Allowing input of the folder name
    
    * Load the seven models (figure 14).
    
      ![image](https://user-images.githubusercontent.com/91185925/137644908-b690664a-8e9b-495d-9f3c-8b7330732372.png)

      Figure 14. Loading the models
    
    * Create lists for each field of logs that I want to select to test (figure 15)
    
      ![image](https://user-images.githubusercontent.com/91185925/137644967-b32733df-0f8d-451e-b62e-a5e072389f08.png)

      Figure 15. The lists in which I put the testing data
    
    * To distinguish two "event" fields, I create two list "X_test_event" (for packetbeat logs) and "X_test_event2" (for winlogbeat logs).
    * Load the json files in the testing folder (figure 16).
    
      ![image](https://user-images.githubusercontent.com/91185925/137644992-3a65e0ee-64bd-467b-90cd-9e6b713f4ad1.png)

      Figure 16. Loading the packetbeat logs of each testcase
    
    * To append the fields of the testing data, I define the functions add_X_Test_p (for packetbeat logs) and add_X_Test_w (for winlogbeat logs). Figure 17 and 18 show the functions.
    
      ![image](https://user-images.githubusercontent.com/91185925/137645019-ec9f2f5c-b6fd-439c-9080-9a6706dc0587.png)

      Figure 17. add_X_test_p
    
      ![image](https://user-images.githubusercontent.com/91185925/137645037-fee6b60d-9518-415b-b985-515af38eaa58.png)

      Figure 18. add_X_test_w
    
    * Append the data of each select fields to the corresponding list (e.g. X_test_type). Repeat the step for each testcase. Figure 19 shows that I call the function add_X_test_p for the fields in packetbeat logs.
    
      ![image](https://user-images.githubusercontent.com/91185925/137645057-cfbaae4a-5c4c-453d-b158-94d9d9268f99.png)

      Figure 19. Calling the function
    
    * Repeat steps f – h for packetbeat logs and winlogbeat logs
    * Use each list to predict the attack type (figure 20).
    
      ![image](https://user-images.githubusercontent.com/91185925/137645120-4b9a215b-9937-44b8-8d96-8f8e7ec2cce6.png)

      Figure 20. Predicting the attack type using each list
    
    * Concatenate the seven results of each list (figure 21).
    
      ![image](https://user-images.githubusercontent.com/91185925/137645139-bca50008-88a8-4341-a738-5d095417559d.png)

      Figure 21. Concatenating the results
    
    * Print the most common element in the result list, which is the attack type I predict for the folder (figure 22).
    
      ![image](https://user-images.githubusercontent.com/91185925/137645154-16f68754-805a-477c-b69f-f02f08f9315a.png)

      Figure 22. Printing the most common element in the result list
    
    * Repeat steps i – l for each testcase.
* Models
  * my_model1: Train with the destination field of the packetbeat logs
  * my_model2: Train with the type field of the packetbeat logs
  * my_model3: Train with the event field of the packetbeat logs
  * my_model4: Train with the source field of the packetbeat logs
  * my_model5: Train with the network field of the packetbeat logs
  * my_model6: Train with the winlog field of the winlogbeat logs
  * my_model7: Train with the event field of the winlogbeat logs

## Reference
* Tree Based Algorithms: A Complete Tutorial from Scratch (in R & Python), ANALYTICS VIDHYA, APRIL 12, 2016. Retrieved from https://www.analyticsvidhya.com/blog/2016/04/tree-based-algorithms-complete-tutorial-scratch-in-python/#one
* The official website of ELK. Retrieved from https://www.elastic.co/
