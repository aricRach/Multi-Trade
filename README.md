# MultiTrade Site 

[![Watch the video](https://i.imgur.com/jm6p70b.jpeg)](https://streamable.com/t47ijc)

Our project will be an internet site written in Python (server-side) and JavaScript (client-side).
The site is providing a comfortable and user-friendly environment for everyone who wants to exchange anything with other users that wants what he offers by using the "trading cycles".
The site suggest exchanging from various types of items like work shifts, personal items,vouchers and more.

First at home page we can find the tenders that open for registration, by clicking the tender's name, we will 

First at home page we can find the tenders that open for registration, by clicking the tender's name, we will move to the tender's page, there we can see the items that participants, by clicking Join we can choose the item that we want participant with and after that we will be part of the tender.
As long as the registration period is not over, the user can choose to exit the tender or replace the item with which he wants to participate with.

As soon as the registration period is over, the item ranking period begins.
In order to show the available items to the user and allow them to select the objects they want over their object, we will display two lists - one of which will be a list of all the objects except the user's item, and the other will be the list of the items  I would like to receive. when wish list is empty at first and we can drag the items we would like to  receive to it,In addition we can change the order of the items in the wish list to determine the order of preference.
If the user regret and want his item he need to click submit when the wish list is empty.

The algorithm can work for a large number of users whenever there is a cycle in the graph which has x people and x items which each wants the other's items, the algorithm will find the largest cycle and then will make the exchange and will continue searching for more cycles for the items that was not exchanged yet. In the "worst case" for a participant, he will stay with his current item.