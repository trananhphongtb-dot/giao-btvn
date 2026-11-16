from tacore import make
U = [
("Unit 1: What's your address?",
 "address=địa chỉ; street=đường phố; village=làng; city=thành phố; flat=căn hộ; house=ngôi nhà; lane=ngõ; quiet=yên tĩnh; crowded=đông đúc; large=rộng; modern=hiện đại; neighbour=hàng xóm",
 """What's your address? - It's 12 Hoa Binh ___.|Street|street's|streets|streeting
I live ___ a flat.|in|on|at|to
Her village is ___. (yên tĩnh)|quiet|crowded|noisy|large
My city is very ___. (đông đúc)|crowded|quiet|small|empty
Where do you live? - I live ___ Thai Binh City.|in|at|on|to
It's a ___ house. (rộng)|large|largely|large's|larger""",
 """Địa chỉ của bạn là gì?|What's your address?
Mình sống ở số 12 đường Hòa Bình.|I live at 12 Hoa Binh Street.
Làng mình rất yên tĩnh.|My village is very quiet.
Thành phố mình đông đúc.|My city is crowded.
Hàng xóm của mình rất tốt bụng.|My neighbours are very kind."""),
("Unit 2: I always get up early",
 "always=luôn luôn; usually=thường xuyên; often=thường; sometimes=thỉnh thoảng; never=không bao giờ; every day=mỗi ngày; get up=ngủ dậy; do morning exercise=tập thể dục buổi sáng; have breakfast=ăn sáng; go to bed=đi ngủ; early=sớm; late=muộn",
 """How often do you get up early? - I ___ get up early.|always|ever|yet|already
He ___ goes to school late. (không bao giờ)|never|always|usually|often
She ___ watches TV in the evening. (thỉnh thoảng)|sometimes|never|always|usually
I do morning exercise ___ day.|every|all|each of|some
I usually ___ my homework after dinner.|do|does|doing|did
My mother ___ cooks dinner. (thường)|usually|ever|never|yet""",
 """Bạn thường làm gì vào buổi sáng?|What do you usually do in the morning?
Mình luôn dậy sớm.|I always get up early.
Bố mình không bao giờ đi làm muộn.|My father never goes to work late.
Mình thỉnh thoảng xem ti vi.|I sometimes watch TV.
Mình tập thể dục mỗi ngày.|I do morning exercise every day."""),
("Unit 3: Where did you go on holiday?",
 "went=đã đi; visited=đã thăm; stayed=đã ở; ate=đã ăn; saw=đã thấy; took=đã chụp/lấy; bought=đã mua; holiday=kỳ nghỉ; island=hòn đảo; cave=hang động; citadel=thành cổ; seafood=hải sản",
 """Where did you go on holiday? - I ___ to Ha Long Bay.|went|go|goes|going
She ___ a lot of photos.|took|take|takes|taking
We ___ seafood on the beach.|ate|eat|eats|eating
I ___ my grandparents last summer.|visited|visit|visits|visiting
Did you enjoy the trip? - Yes, I ___.|did|do|am|was
They ___ at a hotel near the beach.|stayed|stay|stays|staying""",
 """Bạn đã đi đâu vào kỳ nghỉ?|Where did you go on holiday?
Mình đã đến vịnh Hạ Long.|I went to Ha Long Bay.
Chúng mình đã ăn hải sản.|We ate seafood.
Cô ấy đã chụp rất nhiều ảnh.|She took a lot of photos.
Mình đã thăm ông bà mùa hè năm ngoái.|I visited my grandparents last summer."""),
("Unit 4: Did you go to the party?",
 "party=bữa tiệc; invitation=lời mời; birthday=sinh nhật; gift=món quà; cake=bánh ngọt; candle=ngọn nến; balloon=bóng bay; guest=khách mời; sing=hát; dance=nhảy múa; enjoy=thích thú; fun=vui",
 """___ you go to the party? - Yes, I did.|Did|Do|Are|Were
She didn't ___ to the party.|go|went|goes|going
I ___ the party very much. (thích)|enjoyed|enjoy|enjoys|enjoying
We ___ and danced at the party.|sang|sing|sings|singing
What did you do? - I ___ a cake.|ate|eat|eats|eating
The party was ___. (vui)|fun|funny's|funs|funing""",
 """Bạn có đến bữa tiệc không?|Did you go to the party?
Có, mình có đến.|Yes, I did.
Cô ấy không đến bữa tiệc.|She didn't go to the party.
Chúng mình đã hát và nhảy múa.|We sang and danced.
Mình rất thích bữa tiệc.|I enjoyed the party very much."""),
("Unit 5: Where will you be this weekend?",
 "will=sẽ; weekend=cuối tuần; tomorrow=ngày mai; next week=tuần sau; tonight=tối nay; museum=bảo tàng; cinema=rạp chiếu phim; zoo=sở thú; theatre=nhà hát; library=thư viện; stadium=sân vận động; supermarket=siêu thị",
 """Where will you be this weekend? - I ___ be at the zoo.|will|am|do|did
She ___ be at the library tomorrow.|will|is|does|did
What will you do? - I ___ visit my aunt.|will|do|am|did
We will ___ football on Sunday.|play|plays|played|playing
Will you go to the cinema? - Yes, I ___.|will|do|am|did
Will they be at home? - No, they ___.|won't|don't|aren't|didn't""",
 """Cuối tuần này bạn sẽ ở đâu?|Where will you be this weekend?
Mình sẽ ở sở thú.|I will be at the zoo.
Ngày mai cô ấy sẽ ở thư viện.|She will be at the library tomorrow.
Chúng mình sẽ đi rạp chiếu phim.|We will go to the cinema.
Họ sẽ không ở nhà.|They won't be at home."""),
("Unit 6: How many lessons do you have today?",
 "lesson=tiết học; subject=môn học; timetable=thời khóa biểu; Maths=môn Toán; English=môn Tiếng Anh; Science=môn Khoa học; History=môn Lịch sử; Geography=môn Địa lí; IT=môn Tin học; break=giờ ra chơi; homework=bài tập về nhà; exam=bài kiểm tra",
 """___ lessons do you have today? - I have four.|How many|How much|What|Which
I have English twice ___ week.|a|the|an|on
How often do you have Maths? - ___ a week.|Four times|Four time|Fourth|Four
She has ___ lessons in the morning.|three|a|an|the
We have Science ___ Thursday.|on|in|at|to
My favourite subject ___ English.|is|are|am|do""",
 """Hôm nay bạn có bao nhiêu tiết học?|How many lessons do you have today?
Hôm nay mình có bốn tiết.|I have four lessons today.
Mình học tiếng Anh hai lần một tuần.|I have English twice a week.
Môn học yêu thích của mình là môn Khoa học.|My favourite subject is Science.
Chúng mình có bài kiểm tra vào thứ Sáu.|We have a test on Friday."""),
("Unit 7: How do you learn English?",
 "learn=học; practise=luyện tập; speak=nói; listen=nghe; read=đọc; write=viết; vocabulary=từ vựng; pronunciation=phát âm; grammar=ngữ pháp; dictionary=từ điển; club=câu lạc bộ; foreign=nước ngoài",
 """How do you learn English? - I ___ English songs.|listen to|listening|listens|listened
I practise ___ English every day.|speaking|speak|speaks|spoke
She learns vocabulary ___ flashcards.|with|on|at|for
I ___ new words in my notebook.|write|writes|writing|wrote
Why do you learn English? - ___ I want to travel.|Because|But|And|So
Do you go to the English club? - Yes, I ___.|do|am|is|can""",
 """Bạn học tiếng Anh như thế nào?|How do you learn English?
Mình nghe các bài hát tiếng Anh.|I listen to English songs.
Mình luyện nói tiếng Anh mỗi ngày.|I practise speaking English every day.
Mình viết từ mới vào vở.|I write new words in my notebook.
Vì sao bạn học tiếng Anh?|Why do you learn English?"""),
("Unit 8: What are you reading?",
 "story=câu chuyện; fairy tale=truyện cổ tích; comic=truyện tranh; character=nhân vật; kind=tốt bụng; brave=dũng cảm; clever=thông minh; lazy=lười; funny=hài hước; greedy=tham lam; book=quyển sách; author=tác giả",
 """What are you reading? - I'm reading a ___.|story|storing|storied|stories
Tom is ___. (dũng cảm)|brave|lazy|greedy|shy
The fox is ___. (thông minh)|clever|lazy|kind|shy
He doesn't work. He is ___.|lazy|brave|clever|kind
She helps everyone. She is ___.|kind|greedy|lazy|rude
I like the story because it is ___. (hài hước)|funny|fun|funnies|funnily""",
 """Bạn đang đọc gì vậy?|What are you reading?
Mình đang đọc truyện cổ tích.|I'm reading a fairy tale.
Nhân vật chính rất dũng cảm.|The main character is very brave.
Mình thích câu chuyện này vì nó hài hước.|I like this story because it is funny.
Con cáo rất thông minh.|The fox is very clever."""),
("Unit 9: What did you see at the zoo?",
 "see=nhìn thấy; saw=đã nhìn thấy; zoo=sở thú; elephant=con voi; tiger=con hổ; kangaroo=chuột túi; crocodile=cá sấu; peacock=con công; dolphin=cá heo; parrot=con vẹt; wild=hoang dã; dangerous=nguy hiểm",
 """What did you see at the zoo? - I ___ a tiger.|saw|see|sees|seeing
It was a ___ animal. (nguy hiểm)|dangerous|dangerously|danger|dangers
We ___ the peacock dance.|saw|see|sees|seeing
Yesterday I ___ see the elephant. (không thấy)|didn't|don't|doesn't|isn't
Did you see a kangaroo? - Yes, I ___.|did|do|was|am
Elephants are ___ than monkeys. (to hơn)|bigger|big|biggest|more big""",
 """Bạn đã nhìn thấy gì ở sở thú?|What did you see at the zoo?
Mình đã nhìn thấy một con hổ.|I saw a tiger.
Con voi to hơn con khỉ.|The elephant is bigger than the monkey.
Chúng mình đã thấy con công múa.|We saw the peacock dance.
Cá sấu là loài vật nguy hiểm.|Crocodiles are dangerous animals."""),
("Unit 10: Jobs, health and the future",
 "doctor=bác sĩ; engineer=kỹ sư; pilot=phi công; farmer=nông dân; singer=ca sĩ; headache=đau đầu; toothache=đau răng; stomach ache=đau bụng; healthy=khỏe mạnh; exercise=tập thể dục; vegetable=rau củ; future=tương lai",
 """What do you want to be? - I want to be a ___.|pilot|piloting|pilots|piloted
What's the matter? - I have a ___.|headache|head|headaches|headed
You should ___ more vegetables.|eat|eats|eating|ate
You shouldn't ___ too many sweets.|eat|eats|eating|ate
She wants to be a doctor ___ she wants to help sick people.|because|but|so|and
He ___ exercise every morning to stay healthy.|does|do|doing|did""",
 """Bạn muốn làm nghề gì?|What do you want to be?
Mình muốn trở thành phi công.|I want to be a pilot.
Bạn bị làm sao vậy?|What's the matter with you?
Mình bị đau đầu.|I have a headache.
Bạn nên ăn nhiều rau củ.|You should eat more vegetables."""),
]
CHU_DE = make(U)
