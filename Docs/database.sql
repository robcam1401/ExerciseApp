CREATE SCHEMA ExerciseApp;
use ExerciseApp;

-- table creation with attributes
create table UserAccount(
    AccountNumber   int(32)     NOT NULL,
    Username        varchar(15) NOT NULL,
    Email           varchar(32) NOT NULL,
    PhoneNumber     int(11),
    Fname           varchar(15),
    Minit           varchar(1),
    Lname           varchar(15),
    UserDoB         date        NOT NULL,
    constraint User_pk
    primary key (AccountNumber)
    constraint User_unique
    unique (Username, Email, PhoneNumber)
);

create table UserProfile(
    AccountNumber   int(32)     NOT NULL,
    ProfilePic      text(255),
    ProfileBanner   text(255),
    Biography       text(255),
    PhoneNumber     int(11),
    Email           text(50),
    constraint Profile_pk
    primary key (AccountNumber)
);

create table UserSettings(
    AccountNumber   int(32)     NOT NULL,
    AccountPrivacy  int(3)      default 0,
    constraint Settings_pk
    primary key (AccountNumber)
);

create table Videos(
    VideoID         int(32)     NOT NULL,
    VideoLink       text(255)   NOT NULL,
    AccountNumber   int(32)     NOT NULL,
    VideoTitle      text(100)   NOT NULL,
    VidDescription  text(255),
    Category        text(15),
    Views           int(32)     NOT NULL,
    UploadDate      datetime    NOT NULL,
    Thumbnail       text(255)   NOT NULL,
    constraint Video_pk
    primary key (VideoID)
);

create table Comments(
    CommentID       int(32)     NOT NULL,
    AccountNumber   int(32)     NOT NULL,
    CommentBody     text(255)   NOT NULL,
    PostDate        datetime    NOT NULL,
    VideoComment    int(32),    -- used if comment posted under video
    ContentComment  int(32),    -- used if comment posted under content
    ThreadParent    int(32)     NOT NULL, --Parent Comment ID
    Edited          boolean     default false,
    constraint Comment_pk
    primary key (CommentID)
);

create table Content(
    ContentID       int(32)     NOT NULL,
    Category        text(15),
    AccountNumber   int(32)     NOT NULL,
    BodyDescription text(255),
    ContentLink     text(255),
    UploadDate      datetime    NOT NULL,
    constraint Content_pk
    primary key (ContentID)
);

create table Friends(
    User1ID         int(32)     NOT NULL,
    User2ID         int(32)     NOT NULL,
    PairID          int(32)     NOT NULL,
    constraint Friends_pk
    primary key (PairID)
);

create table FriendMessages(
    PairID          int(32)     NOT NULL,
    MessageID       int(32)     NOT NULL,
    MessageBody     text(255)   NOT NULL,
    SentStamp       datetime    NOT NULL,
    SentUser        int(32)     NOT NULL,
    AttatchedLink   text(255),
    constraint FriendMessages_pk
    primary key (MessageID)
);

create table Communities(
    CommunityID     int(32)     NOT NULL,
    CommName        text(25)    NOT NULL,
    CommDescription text(255),
    CreatedUser     int(32)     NOT NULL,
    constraint Communities_pk
    primary key (CommunityID)
);

create table CommMessages(
    CommunityID     int(32)     NOT NULL,
    MessageID       int(32)     NOT NULL,
    MessageBody     text(255)   NOT NULL,
    AttatchedLink   text(255),
    SentStamp       datetime    NOT NULL,
    SentUser        int(32)     NOT NULL,
    constraint CommMessages_pk
    primary key (MessageID)
);

create table Events(
    EventID         int(32)     NOT NULL,
    EventName       text(25)    NOT NULL,
    EventDesc       text(255),
    PostTime        datetime    NOT NULL,
    StartTime       datetime    NOT NULL,
    EventLocation   text(255)   NOT NULL,
    PosterID        int(32)     NOT NULL,
    Category        text(15),
    constraint Event_pk
    primary key (EventID)
);

-- modify tables to create constraints with foreign keys

    -- Keys connect Video(AccountNumber) to USerAccount(AccountNumber)
alter table Video
    add constraint video_owner_fk
    foreign key (AccountNumber) references UserAccount(AccountNumber)

    -- Keys connect UserProfile(AccountNumber) to UserAccount(AccountNumber)
alter table UserProfile
    add constraint profile_fk
    foreign key (AccountNumber) references UserAccount(AccountNumber)

    -- Keys connect UserSettings(AccountNumber) to UserAccount(AccountNumber)
alter table UserSettings
    add constraint settings_fk
    foreign key (AccountNumber) references UserAccount(AccountNumber)

    -- Keys connect Comments(AccountNumber) to UserAccount(AccountNumber)
    --              Comments(VideoComment) to Video(VideoID)
    --              Comments(ContentComment) to Content(ContentID)
    --              Comments(ThreadParent) to Comment(CommentID)
alter table Comments
    add constraint comment_owner_fk
    foreign key (AccountNumber) references UserAccount(AccountNumber)
    add constraint video_comment_fk
    foreign key (VideoComment) references Video(VideoID)
    add constraint content_comment_fk
    foreign key (ContentComment) references Content(ContentID)
    add constraint thread_fk
    foreign key (ThreadParent) references Comment(CommentID)

    -- Keys connect Content(AccountNumber) to UserAccount(AccountNumber)
alter table Content
    add constraint content_owner_fk
    foreign key (AccountNumber) references UserAccount(AccountNumber)

    -- Keys connect Friends(User1) to UserAccount(AccountNumber)
    --              Friends(User2) to UserAccount(AccountNumber)
alter table Friends
    add constraint user1_fk
    foreign key (User1) references UserAccount(AccountNumber)
    add constraint user2_fk
    foreign key (User2) references UserAccount(AccountNumber)

    -- Keys connect FriendMessages(PairID) to Friends(PairID)
    --              FriendMessages(SentUser) to UserAccount(AccountNumber)
alter table FriendMessages
    add constraint friend_pair_fk
    foreign key (PairID) references Friends(PairID)
    add constraint sent_user_fk
    foreign key (SentUser) references UserAccount(AccountNumber)

    -- Keys connect Communities(CreatedUser) to UserAccount(AccountNumber)
alter table Communities
    add constraint created_user_fk
    foreign key (CreatedUser) references UserAccount(AccountNumber)

    -- Keys connect CommMessages(CommunityID) to Communities(CommunityID)
    --              CommMessages(SentUser) to UserAccount(AccountNumber)
alter table CommMessages
    add constraint comm_id_fk
    foreign key (CommunityID) references Community(CommunityID)
    
    -- Keys connect Events(PosterID) to UserAccount(AccountNumber)
alter table Events
    add constraint poster_id_fk
    foreign key (PosterID) references UserAccount(AccountNumber)
