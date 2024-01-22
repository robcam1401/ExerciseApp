USE ExerciseApp

/* Given a creator ID, retrieve all of the videos that creator has posted
Will include different sorting functions, UploadDate, Title, Views, etc.
video can be swapped for content/comments
*/
create view UserVids
DECLARE @Creator AS int(32) = 0;
SELECT v.VideoID, v.VideoLink, v.AccountNumber v.VideoTitle, v.Thumbnail, v.Views, v.UploadDate, u.AccountNumber
FROM video V, UserAccount u
WHERE @Creator = u.UserAccount = v.UserAccount
GROUP BY v.UploadDate;

/* Given a User, retrieve all of their friend pairs
Sort by last message sent/received, alphabetically, etc.
*/
create view UserFriends
DECLARE @User AS int(32) = 0;
SELECT f.User1ID, f.User2ID, f.PairID, u.UserAccount
WHERE @User = u.UserAccount and (u.UserAccount = (f.User1ID or f.User2ID));

/* Given a community, retrieve all of the messages sent in the community chat
Sort by last sent
*/
create view CommunityMessages
DECLARE @Community AS int(32) = 0;
SELECT m.CommunityID, m.MessageID, m.MessageBody, m.SentStamp, m.SentUser
WHERE @Community = m.CommunityID
GROUP BY m.SentStamp