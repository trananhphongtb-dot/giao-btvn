from tacore import make
U = [
("Unit 1: In the school playground",
 "playground=sân chơi; school=trường học; library=thư viện; gym=phòng thể dục; music room=phòng nhạc; classroom=lớp học; playing=đang chơi; skipping=nhảy dây; football=bóng đá; hide-and-seek=trốn tìm; run=chạy; friends=những người bạn",
 """This is my ___. (trường học)|school|house|garden|park
She is ___ in the playground. (nhảy dây)|skipping|reading|eating|sleeping
They are playing ___. (bóng đá)|football|the piano|the guitar|chess
We are in the ___. (thư viện)|library|kitchen|bedroom|bathroom
What are you doing? - I'm ___.|playing|play|plays|played
Where is Nam? - He is in the ___.|playground|bag|pen|book""",
 """Đây là sân trường của mình.|This is my school playground.
Các bạn đang chơi bóng đá.|The children are playing football.
Mình thích chơi trốn tìm.|I like playing hide-and-seek.
Bạn đang làm gì?|What are you doing?
Mình đang đọc sách trong thư viện.|I'm reading a book in the library."""),
("Unit 2: My house",
 "house=ngôi nhà; living room=phòng khách; bedroom=phòng ngủ; kitchen=nhà bếp; bathroom=phòng tắm; garden=khu vườn; table=cái bàn; sofa=ghế sô-pha; bed=cái giường; lamp=cái đèn; TV=ti vi; window=cửa sổ",
 """I sleep in the ___. (phòng ngủ)|bedroom|kitchen|garden|bathroom
Mum cooks in the ___. (nhà bếp)|kitchen|bedroom|living room|garden
We watch TV in the ___. (phòng khách)|living room|bathroom|kitchen|garden
Where is the cat? - It's ___ the table. (dưới)|under|on|in|behind
The lamp is ___ the table. (trên)|on|under|in|behind
There ___ a sofa in the living room.|is|are|am|be""",
 """Nhà mình có bốn phòng.|My house has four rooms.
Có một chiếc giường trong phòng ngủ.|There is a bed in the bedroom.
Mẹ nấu ăn trong bếp.|Mum cooks in the kitchen.
Con mèo ở dưới bàn.|The cat is under the table.
Chiếc đèn ở trên bàn.|The lamp is on the table."""),
("Unit 3: My school things and toys",
 "notebook=quyển vở; pencil case=hộp bút; schoolbag=cặp sách; marker=bút lông; sharpener=gọt bút chì; glue=hồ dán; scissors=cái kéo; paper=giấy; paint=màu vẽ; brush=cọ vẽ; toy=đồ chơi; robot=người máy",
 """I need ___ to cut paper. (kéo)|scissors|glue|a ruler|a bag
I put my pens in the ___. (hộp bút)|pencil case|desk|window|chair
Is this your notebook? - Yes, it ___.|is|are|am|do
Are these your pencils? - Yes, they ___.|are|is|am|do
These ___ my markers.|are|is|am|be
This ___ my glue.|is|are|am|be""",
 """Đây là vở của mình.|This is my notebook.
Đây là những cây bút lông của mình.|These are my markers.
Mình cần cái kéo.|I need a pair of scissors.
Đó là cái cặp của bạn à?|Is that your schoolbag?
Không, đó không phải cặp của mình.|No, it isn't."""),
("Unit 4: My family and my pets",
 "parents=bố mẹ; brother=anh/em trai; sister=chị/em gái; grandparents=ông bà; uncle=chú/bác; aunt=cô/dì; cousin=anh chị em họ; pet=thú cưng; puppy=chó con; kitten=mèo con; parrot=con vẹt; goldfish=cá vàng",
 """She is my mother's sister. She is my ___.|aunt|uncle|cousin|brother
He is my father's brother. He is my ___.|uncle|aunt|sister|grandmother
How many people are there in your family? - There ___ four.|are|is|am|be
I have a pet ___. (chó con)|puppy|kitten|parrot|goldfish
My grandparents ___ old.|are|is|am|be
Do you have a pet? - Yes, I ___.|do|am|is|are""",
 """Gia đình mình có bốn người.|There are four people in my family.
Mình có một chú mèo con.|I have a kitten.
Ông bà mình sống ở quê.|My grandparents live in the countryside.
Con vẹt của mình biết nói.|My parrot can talk.
Chú chó con đang chạy.|The puppy is running."""),
("Unit 5: Food, drinks and clothes",
 "rice=cơm; noodles=mì; soup=súp; sandwich=bánh mì kẹp; juice=nước ép; milk=sữa; T-shirt=áo phông; dress=váy liền; jacket=áo khoác; shoes=giày; hat=mũ; socks=tất",
 """I'm thirsty. I'd like some ___.|juice|noodles|rice|soup
I'm cold. I put on my ___. (áo khoác)|jacket|T-shirt|socks|hat
She wears a ___. (váy liền)|dress|shoes|socks|hat
Would you like some milk? - Yes, ___.|please|hello|sorry|goodbye
Would you like some soup? - No, ___.|thank you|please|hello|sorry
I wear ___ on my feet. (giày)|shoes|a hat|a dress|a jacket""",
 """Bạn muốn uống chút sữa không?|Would you like some milk?
Vâng, cảm ơn.|Yes, please.
Mình muốn ăn mì.|I'd like some noodles.
Mình đội mũ.|I wear a hat.
Cô ấy mặc váy.|She wears a dress."""),
("Unit 6: Animals and body",
 "tiger=con hổ; lion=sư tử; zebra=ngựa vằn; giraffe=hươu cao cổ; crocodile=cá sấu; snake=con rắn; tail=cái đuôi; wing=cái cánh; paw=chân (thú); long=dài; short=ngắn; big=to",
 """A giraffe has a ___ neck. (dài)|long|short|small|round
A bird has two ___. (cánh)|wings|tails|paws|hands
A tiger ___ run fast.|can|is|are|does
A snake ___ fly.|can't|am|are|is
What can a monkey do? - It can ___.|climb|climbs|climbing|climbed
Is it big? - Yes, it ___.|is|are|am|do""",
 """Con hổ chạy rất nhanh.|The tiger runs very fast.
Con rắn không biết bay.|A snake can't fly.
Hươu cao cổ có cổ dài.|A giraffe has a long neck.
Con khỉ biết trèo cây.|A monkey can climb trees.
Con sư tử rất to.|The lion is very big."""),
("Unit 7: Weather and seasons",
 "weather=thời tiết; sunny=có nắng; rainy=có mưa; windy=có gió; cloudy=có mây; snowy=có tuyết; spring=mùa xuân; summer=mùa hè; autumn=mùa thu; winter=mùa đông; umbrella=cái ô; raincoat=áo mưa",
 """What's the weather like? - It's ___. (có mưa)|rainy|sunny|snowy|hot
It's rainy. I need an ___.|umbrella|bag|ice cream|hat
Ice cream is good in ___. (mùa hè)|summer|winter|rain|snow
It's cold in ___. (mùa đông)|winter|summer|spring|sun
Flowers bloom in ___. (mùa xuân)|spring|winter|autumn|snow
I go to the beach when it's ___.|sunny|snowy|rainy|cold""",
 """Hôm nay thời tiết thế nào?|What's the weather like today?
Trời đang mưa.|It's raining.
Mùa hè trời nóng.|It's hot in summer.
Mình thích mùa xuân.|I like spring.
Mình cần một chiếc ô.|I need an umbrella."""),
("Unit 8: Jobs and places",
 "teacher=giáo viên; doctor=bác sĩ; nurse=y tá; farmer=nông dân; driver=tài xế; cook=đầu bếp; hospital=bệnh viện; farm=nông trại; market=chợ; shop=cửa hàng; park=công viên; zoo=sở thú",
 """A ___ works in a hospital. (bác sĩ)|doctor|farmer|driver|cook
A ___ works on a farm. (nông dân)|farmer|doctor|nurse|teacher
A ___ teaches students. (giáo viên)|teacher|cook|driver|farmer
My father is a driver. He ___ a car.|drives|drive|driving|drove
Where does your mother work? - She works in a ___.|hospital|garden|toy|bag
What does your father do? - He is a ___.|farmer|farm|farms|farming""",
 """Bố mình là bác sĩ.|My father is a doctor.
Mẹ mình là giáo viên.|My mother is a teacher.
Bác ấy làm việc ở nông trại.|He works on a farm.
Mình đi chợ cùng mẹ.|I go to the market with my mother.
Chúng mình đi sở thú.|We go to the zoo."""),
("Unit 9: Daily activities",
 "wake up=thức dậy; get up=ngủ dậy; brush teeth=đánh răng; have breakfast=ăn sáng; go to school=đi học; do homework=làm bài tập; have dinner=ăn tối; go to bed=đi ngủ; watch TV=xem ti vi; read a book=đọc sách; play=chơi; help mum=giúp mẹ",
 """I ___ up at six o'clock. (thức dậy)|wake|wakes|waking|woke
She ___ her teeth every morning.|brushes|brush|brushing|brushed
He ___ to school at seven.|goes|go|going|gone
What time do you go to bed? - I go to bed ___ nine.|at|on|in|to
I do my homework ___ the evening.|in|on|at|to
They ___ breakfast at 6:30.|have|has|having|had""",
 """Mình thức dậy lúc sáu giờ.|I wake up at six o'clock.
Mình đánh răng mỗi sáng.|I brush my teeth every morning.
Mình đi học lúc bảy giờ.|I go to school at seven.
Mình làm bài tập vào buổi tối.|I do my homework in the evening.
Mình đi ngủ lúc chín giờ.|I go to bed at nine."""),
("Unit 10: Hobbies and abilities",
 "swim=bơi; ride a bike=đi xe đạp; draw=vẽ; sing=hát; dance=múa; cook=nấu ăn; play the piano=chơi đàn piano; play football=chơi bóng đá; read=đọc; write=viết; fly a kite=thả diều; take photos=chụp ảnh",
 """I like ___. (vẽ)|drawing|draw|draws|drew
She can ___ well. (hát)|sing|sings|singing|sang
Can he swim? - Yes, he ___.|can|does|is|do
Can they dance? - No, they ___.|can't|don't|aren't|isn't
My hobby is ___ photos. (chụp ảnh)|taking|take|takes|took
I ___ play the piano. (không biết)|can't|don't|am not|isn't""",
 """Sở thích của mình là vẽ tranh.|My hobby is drawing.
Mình biết bơi.|I can swim.
Em gái mình biết hát.|My sister can sing.
Bạn có biết chơi đàn không?|Can you play the piano?
Mình thích thả diều.|I like flying kites."""),
]
CHU_DE = make(U)
