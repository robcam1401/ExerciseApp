USE ExerciseApp;

/* Each table has a key identifier that will count up from the first post
Additionally, a new row in UserProfile and UserSettings will be created
*/


drop trigger if exists `NewUser`;
DELIMITER ;;
create trigger NewUser
    Before insert on UserAccount
    for each row
    BEGIN
        insert into UserProfile
        values (AccountNumber, NEW.AccountNumber);
        insert into UserSettings
        values (AccountNumber, NEW.AccountNumber);
    END;;
DELIMITER ;

drop trigger if exists `NewVideo`;
DELIMITER ;;
create trigger NewVideo
    Before insert on Videos
    for each row
    BEGIN
        set NEW.UploadDate = GETDATE();
    END;;
DELIMITER ;

drop trigger if exists `NewComment`;
DELIMITER ;;
create trigger NewComment
    Before insert on Comments
    for each row
    BEGIN
        set NEW.PostDate = GETDATE();
    END;;
DELIMITER ;

drop trigger if exists `NewContent`;
DELIMITER ;;
create trigger NewContent
    Before insert on Content
    for each row
    BEGIN
        set NEW.UploadDate = GETDATE();
    END;;
DELIMITER ;

drop trigger if exists `NewMessages`;
DELIMITER ;;
create trigger NewMessages
    Before insert on FriendMessages
    for each row
    BEGIN
        set NEW.SentStamp = GETDATE();
    END;;
DELIMITER ;

drop trigger if exists `NewCommMessage`;
DELIMITER ;;
create trigger NewCommMessage
    Before insert on CommMessages
    for each row
    BEGIN
        set NEW.SentStamp = GETDATE();
    END;;
DELIMITER ;

drop trigger if exists `NewEvent`;
DELIMITER ;;
create trigger NewEvent
    Before insert on Events
    for each row
    BEGIN
        set NEW.PostTime = GETDATE();
    END;;
DELIMITER ;