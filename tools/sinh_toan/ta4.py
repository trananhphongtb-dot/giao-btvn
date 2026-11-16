from tacore import make
U = [
("Unit 1: Nice to see you again",
 "again=lại; nice=tốt đẹp; see=nhìn thấy; holiday=kỳ nghỉ; summer=mùa hè; fine=khỏe; later=sau; late=muộn; welcome=chào mừng; class=lớp học; classmate=bạn cùng lớp; back=trở lại",
 """Nice to see you ___.|again|late|back|fine
How are you? - I'm ___, thank you.|fine|name|class|teacher
Welcome ___ to school.|back|late|at|up
See you ___.|later|late|lately|last
I ___ a student at Hoa Sen school.|am|is|are|be
They ___ my classmates.|are|is|am|be""",
 """Rất vui được gặp lại bạn.|Nice to see you again.
Bạn khỏe không?|How are you?
Chào mừng các bạn trở lại trường.|Welcome back to school.
Hẹn gặp lại sau nhé.|See you later.
Họ là bạn cùng lớp của mình.|They are my classmates."""),
("Unit 2: I'm from Japan",
 "Vietnam=Việt Nam; Viet Nam=Việt Nam; Japan=Nhật Bản; America=nước Mỹ; England=nước Anh; Australia=nước Úc; Malaysia=Ma-lai-xi-a; Singapore=Xin-ga-po; country=đất nước; nationality=quốc tịch; Vietnamese=người Việt Nam; Japanese=người Nhật",
 """Where are you from? - I'm ___ Viet Nam.|from|in|at|on
___ is she from? - She's from Japan.|Where|What|Who|When
What nationality are you? - I'm ___.|Vietnamese|Viet Nam|Vietnam's|Vietnams
He is from England. He is ___.|English|England|Englands|Englishs
Are you from Australia? - Yes, I ___.|am|do|is|are
Is she from Malaysia? - No, she ___.|isn't|aren't|doesn't|am not""",
 """Bạn đến từ đâu?|Where are you from?
Mình đến từ Việt Nam.|I'm from Viet Nam.
Cô ấy đến từ Nhật Bản.|She is from Japan.
Quốc tịch của bạn là gì?|What nationality are you?
Mình là người Việt Nam.|I'm Vietnamese."""),
("Unit 3: What day is it today?",
 "Monday=thứ Hai; Tuesday=thứ Ba; Wednesday=thứ Tư; Thursday=thứ Năm; Friday=thứ Sáu; Saturday=thứ Bảy; Sunday=Chủ nhật; week=tuần; today=hôm nay; tomorrow=ngày mai; weekend=cuối tuần; day=ngày",
 """What day is it today? - It's ___.|Monday|January|morning|July
Today is Friday. Tomorrow is ___.|Saturday|Thursday|Monday|Sunday
I have English ___ Monday.|on|in|at|to
I go to school ___ Monday to Friday.|from|at|in|on
What do you do on Sundays? - I ___ my grandparents.|visit|visits|visiting|visited
She ___ to school on Saturdays.|doesn't go|don't go|doesn't goes|not go""",
 """Hôm nay là thứ mấy?|What day is it today?
Hôm nay là thứ Hai.|It's Monday today.
Mình có môn tiếng Anh vào thứ Ba.|I have English on Tuesday.
Chủ nhật mình đi thăm ông bà.|I visit my grandparents on Sundays.
Mình đi học từ thứ Hai đến thứ Sáu.|I go to school from Monday to Friday."""),
("Unit 4: When's your birthday?",
 "January=tháng Một; February=tháng Hai; March=tháng Ba; April=tháng Tư; May=tháng Năm; June=tháng Sáu; July=tháng Bảy; August=tháng Tám; September=tháng Chín; October=tháng Mười; November=tháng Mười Một; December=tháng Mười Hai",
 """When's your birthday? - It's ___ May.|in|on|at|to
It's on the ___ of June. (ngày 5)|fifth|five|fiftieth|fives
My birthday is on the ___ of March. (ngày 1)|first|one|oneth|once
The month after July is ___.|August|June|September|May
The month before April is ___.|March|May|June|February
Happy ___! (Chúc mừng sinh nhật)|birthday|holiday|Sunday|school""",
 """Sinh nhật bạn là khi nào?|When's your birthday?|
Sinh nhật mình vào tháng Năm.|My birthday is in May.
Sinh nhật mình vào ngày mùng hai tháng Tư.|My birthday is on the second of April.
Chúc mừng sinh nhật bạn!|Happy birthday to you!
Bạn bao nhiêu tuổi?|How old are you?"""),
("Unit 5: Can you swim?",
 "swim=bơi; skate=trượt patin; skip=nhảy dây; cook=nấu ăn; draw=vẽ; sing=hát; dance=nhảy múa; ride a bike=đạp xe; play chess=chơi cờ; play the piano=chơi đàn piano; play the guitar=chơi đàn ghi-ta; fly a kite=thả diều",
 """Can you swim? - Yes, I ___.|can|do|am|is
Can he skate? - No, he ___.|can't|doesn't|isn't|don't
I can ___ the piano.|play|plays|playing|played
She can ___ well. (hát)|sing|sings|singing|sang
What can you do? - I can ___.|draw|draws|drawing|drew
___ you cook? - Yes, I can.|Can|Do|Are|Is""",
 """Bạn có biết bơi không?|Can you swim?
Vâng, mình biết bơi.|Yes, I can.
Em trai mình không biết trượt patin.|My brother can't skate.
Bạn biết làm gì?|What can you do?
Mình biết chơi đàn ghi-ta.|I can play the guitar."""),
("Unit 6: Where's your school?",
 "school=trường học; street=đường phố; road=con đường; village=làng; town=thị trấn; city=thành phố; district=quận/huyện; big=to; small=nhỏ; beautiful=đẹp; near=gần; far=xa",
 """Where's your school? - It's in Hoa Binh ___.|Street|street's|Streets|Streeting
Is your school big? - Yes, it ___.|is|are|am|does
My school is ___ my house. (gần)|near|far|big|small
What's your school like? - It's ___.|beautiful|where|who|when
My school ___ in a village.|is|are|am|be
The school is ___ the park. (đối diện)|opposite|on|at|to""",
 """Trường bạn ở đâu?|Where's your school?
Trường mình ở đường Hòa Bình.|My school is on Hoa Binh Street.
Trường mình rất đẹp.|My school is very beautiful.
Trường mình gần nhà mình.|My school is near my house.
Trường bạn như thế nào?|What's your school like?"""),
("Unit 7: What do you like doing?",
 "reading=đọc sách; swimming=bơi lội; cycling=đạp xe; fishing=câu cá; gardening=làm vườn; collecting stamps=sưu tầm tem; going shopping=đi mua sắm; taking photos=chụp ảnh; listening to music=nghe nhạc; watching TV=xem ti vi; hobby=sở thích; free time=thời gian rảnh",
 """What do you like doing? - I like ___.|reading|read|reads|to reading
She likes ___ photos.|taking|take|takes|took
What's your ___? - My hobby is swimming.|hobby|name|age|school
My brother likes ___ to music.|listening|listen|listens|listened
What does he like doing? - He ___ fishing.|likes|like|liking|liked
They like ___ stamps.|collecting|collect|collects|collected""",
 """Bạn thích làm gì?|What do you like doing?
Mình thích đọc sách.|I like reading.
Chị mình thích chụp ảnh.|My sister likes taking photos.
Sở thích của mình là câu cá.|My hobby is fishing.
Bố mình thích làm vườn.|My father likes gardening."""),
("Unit 8: What subjects do you have today?",
 "Maths=môn Toán; Vietnamese=môn Tiếng Việt; English=môn Tiếng Anh; Science=môn Khoa học; Music=môn Âm nhạc; Art=môn Mĩ thuật; PE=môn Thể dục; IT=môn Tin học; subject=môn học; timetable=thời khóa biểu; lesson=bài học; today=hôm nay",
 """What subjects do you have today? - I have ___.|Maths|Monday|morning|Friday
I have PE ___ Tuesday.|on|in|at|to
When do you have Music? - I have it on ___.|Wednesday|Maths|English|Art
Why do you like Art? - Because I can ___.|draw|drawing|draws|drew
What subject do you like? - I like ___.|Science|Sundays|school|lunch
She ___ English on Mondays.|has|have|having|had""",
 """Hôm nay bạn có những môn gì?|What subjects do you have today?
Hôm nay mình có môn Toán và môn Tiếng Anh.|I have Maths and English today.
Mình thích môn Mĩ thuật.|I like Art.
Bạn có môn Âm nhạc khi nào?|When do you have Music?
Mình có môn Thể dục vào thứ Ba.|I have PE on Tuesday."""),
("Unit 9: What are they doing?",
 "reading=đang đọc; writing=đang viết; drawing=đang vẽ; listening=đang nghe; playing=đang chơi; cooking=đang nấu ăn; watching=đang xem; singing=đang hát; dancing=đang nhảy; skipping=đang nhảy dây; running=đang chạy; painting=đang tô vẽ",
 """What is he doing? - He ___ a book.|is reading|reads|read|reading
What are they doing? - They ___ football.|are playing|is playing|plays|play
She is ___ a song.|singing|sing|sings|sang
We are ___ in the playground.|running|run|runs|ran
My mother is ___ in the kitchen.|cooking|cook|cooks|cooked
I am ___ TV now.|watching|watch|watches|watched""",
 """Anh ấy đang làm gì?|What is he doing?
Anh ấy đang đọc sách.|He is reading a book.
Họ đang chơi bóng đá.|They are playing football.
Mẹ mình đang nấu ăn.|My mother is cooking.
Chúng mình đang chạy ngoài sân.|We are running in the playground."""),
("Unit 10: Where were you yesterday?",
 "yesterday=hôm qua; last week=tuần trước; was=đã ở (số ít); were=đã ở (số nhiều); zoo=sở thú; beach=bãi biển; farm=nông trại; park=công viên; museum=bảo tàng; cinema=rạp chiếu phim; mountain=ngọn núi; weekend=cuối tuần",
 """Where ___ you yesterday? - I was at the zoo.|were|was|are|is
I ___ at the beach yesterday.|was|were|am|is
They ___ at the museum last week.|were|was|are|am
___ she at home yesterday? - No, she wasn't.|Was|Were|Is|Did
We ___ at the park on Sunday.|were|was|are|is
He ___ at the cinema last Saturday.|was|were|is|are""",
 """Hôm qua bạn ở đâu?|Where were you yesterday?
Hôm qua mình ở sở thú.|I was at the zoo yesterday.
Họ ở bảo tàng tuần trước.|They were at the museum last week.
Cô ấy không ở nhà hôm qua.|She wasn't at home yesterday.
Cuối tuần trước chúng mình ở bãi biển.|We were at the beach last weekend."""),
]
CHU_DE = make(U)
