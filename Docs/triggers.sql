USE ExerciseApp

/* Each table has a key identifier that will count up from the first post
Additionally, a new row in UserProfile and UserSettings will be created
*/

create trigger NewUser
    Before insert on UserAccount
    for each row
    BEGIN
        if (NEW.AccountNumber = '' or NEW.AccountNumber is NULL)
        then
        set(NEW.AccountNumber = SELECT MAX(AccountNumber) + 1)
        insert into UserProfile
        values (AccountNumber, NEW.AccountNumber)
        insert into UserSettings
        values (AccountNumber, NEW.AccountNumber)
        end if;
        

create trigger NewVideo
    Before insert on Videos
    for each row
    BEGIN
        if (NEW.VideoID = '' or NEW.VideoID is NULL)
        then
        set(NEW.VideoID = SELECT MAX(VideoID) + 1)
        end if;

create trigger NewComment
    Before insert on Comments
    for each row
    BEGIN
        if (NEW.CommentID = '' or NEW.CommentID is NULL)
        then
        set(NEW.CommentID = SELECT MAX(CommentID) + 1)
        end if;

create trigger NewContent
    Before insert on Content
    for each row
    BEGIN
        if (NEW.ContentID = '' or NEW.ContentID is NULL)
        then
        set(NEW.ContentID = SELECT MAX(ContentID) + 1)
        end if;

create trigger NewFriends
    Before insert on Friends
    for each row
    BEGIN
        if (NEW.PairID = '' or NEW.PairID is NULL)
        then
        set(NEW.PairID = SELECT MAX(PairID) + 1)
        end if;

create trigger NewMessages
    Before insert on FriendMessages
    for each row
    BEGIN
        if (NEW.MessageID = '' or NEW.MessageID is NULL)
        then
        set(NEW.MessageID = SELECT MAX(MessageID) + 1)
        end if;

create trigger NewCommunity
    Before insert on Communities
    for each row
    BEGIN
        if (NEW.CommunityID = '' or NEW.CommunityID is NULL)
        then
        set(NEW.CommunityID = SELECT MAX(CommunityID) + 1)
        end if;

create trigger NewCommMessage
    Before insert on CommMessages
    for each row
    BEGIN
        if (NEW.MessageID = '' or NEW.MessageID is NULL)
        then
        set(NEW.MessageID = SELECT MAX(MessageID) + 1)
        end if;

create trigger NewEvent
    Before insert on Events
    for each row
    BEGIN
        if (NEW.EventID = '' or NEW.EventID is NULL)
        then
        set(NEW.EventID = SELECT MAX(EventID) + 1)
        end if;