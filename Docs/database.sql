CREATE SCHEMA database;
use database;

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

create table Videos(
    VideoID         int(32)     NOT NULL,
    VideoLink       text(255)   NOT NULL,
    AccountNumber   int(32)     NOT NULL,
    VideoTitle      text(100)   NOT NULL,
    VidDescription  text(255),
    Category        text(15),
    Views           int(32)     NOT NULL,
    UploadDate      datetime    NOT NULL,
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
    pairID          int(32)     NOT NULL,
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

alter table Video
    add constraint video_owner_fk
    foreign key (AccountNumber) references UserAccount(AccountNumber)
    on delete set NULL
    on update cascade;

alter table Comments
    add constraint comment_owner_fk
    foreign key (AccountNumber) references UserAccount(AccountNumber)
    add constraint video_comment_fk
    foreign key (VideoComment) references Video(VideoID)
    add constraint content_comment_fk
    foreign key (ContentComment) references Content(ContentID)
    add constraint thread_fk
    foreign key (ThreadParent) references Comment(CommentID)

alter table content
    add constraint content_owner_fk
    foreign key (AccountNumber) references UserAccount(AccountNumber)

alter table Friends
    add constraint user1_fk
    foreign key (User1) references UserAccount(AccountNumber)
    add constraint user2_fk
    foreign key (User2) references UserAccount(AccountNumber)

alter table FriendMessages
    add constraint friend_pair_fk
    foreign key (PairID) references Friends(PairID)
    add constraint sent_user_fk
    foreign key (SentUser) references UserAccount(AccountNumber)

alter table Communities
    add constraint created_user_fk
    foreign key (CreatedUser) references UserAccount(AccountNumber)
