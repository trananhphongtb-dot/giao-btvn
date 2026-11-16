from tacore import make
U = [
("Unit 1: Hello",
 "hello=xin chào; hi=chào; goodbye=tạm biệt; nice to meet you=rất vui được gặp bạn; fine=khỏe; thanks=cảm ơn; how=thế nào; teacher=giáo viên; student=học sinh; class=lớp học; meet=gặp; name=tên",
 """___ are you? - I'm fine, thanks.|How|What|Who|Where
Nice to ___ you.|meet|meets|meeting|met
Hello, I ___ Nam.|am|is|are|be
Hi, ___ name is Mai.|my|me|I|am
What's your name? - ___ name is Lan.|My|I|Me|Am
Goodbye, Nam. - ___, Mai.|Bye|Hello|Hi|Thanks""",
 """Chào bạn, mình là Nam.|Hello, I'm Nam.
Bạn khỏe không?|How are you?
Mình khỏe, cảm ơn bạn.|I'm fine, thank you.
Rất vui được gặp bạn.|Nice to meet you.
Tạm biệt, hẹn gặp lại.|Goodbye. See you later."""),
("Unit 2: Our names",
 "name=tên; spell=đánh vần; letter=chữ cái; surname=họ; first name=tên riêng; alphabet=bảng chữ cái; write=viết; call=gọi; Mr=ông; Miss=cô/bà; again=lại; please=làm ơn",
 """What's your name? - ___ Linh.|I'm|It|He|You
How do you ___ your name?|spell|spells|spelling|spelled
___ is your name? - It's Tom.|What|Who|How|Where
Can you spell your name, ___?|please|hello|bye|sorry
Hi, Mai. Hello, Nam. - They are ___.|friends|name|teacher|desk
How do you spell "cat"? - C-A-___.|T|P|N|R""",
 """Tên bạn là gì?|What's your name?
Bạn đánh vần tên bạn thế nào?|How do you spell your name?
Tên mình là Hoa.|My name is Hoa.
Bạn có thể đánh vần lại không?|Can you spell it again, please?
Mình viết tên của mình.|I write my name."""),
("Unit 3: Our friends",
 "friend=bạn; boy=con trai; girl=con gái; he=anh ấy; she=cô ấy; this=đây; that=kia; new=mới; old=cũ/già; tall=cao; short=thấp; nice=tốt bụng",
 """Who is that? - ___ is Nam.|He|She|It|They
Who is that girl? - ___ is Mai.|She|He|It|They
___ is my new friend. (Đây)|This|That|These|Those
That ___ my teacher.|is|are|am|be
Is he your friend? - Yes, he ___.|is|are|am|does
Is she tall? - No, she ___.|isn't|aren't|am not|doesn't""",
 """Đây là bạn mới của mình.|This is my new friend.
Cậu bé kia là ai?|Who is that boy?
Bạn ấy là Nam.|He is Nam.
Cô ấy là bạn của mình.|She is my friend.
Bạn ấy cao và tốt bụng.|She is tall and nice."""),
("Unit 4: Our bodies",
 "head=đầu; eyes=mắt; ears=tai; nose=mũi; mouth=miệng; hands=hai bàn tay; arms=hai cánh tay; legs=hai chân; feet=hai bàn chân; fingers=ngón tay; toes=ngón chân; body=cơ thể",
 """I have two ___. (mắt)|eyes|noses|mouths|heads
I have one ___. (mũi)|nose|ears|eyes|hands
Touch your ___. (đầu)|head|book|desk|bag
These are my ___. (bàn tay)|hands|foot|ear|nose
I see with my ___.|eyes|ears|mouth|feet
I listen with my ___.|ears|eyes|nose|hands""",
 """Đây là cái đầu của mình.|This is my head.
Đây là những ngón tay của mình.|These are my fingers.
Mình có hai bàn tay.|I have two hands.
Bạn chạm vào mũi đi.|Touch your nose.
Mình dùng tai để nghe.|I listen with my ears."""),
("Unit 5: My hobbies",
 "hobby=sở thích; swimming=bơi lội; cycling=đạp xe; painting=vẽ tranh; cooking=nấu ăn; reading=đọc sách; singing=ca hát; dancing=nhảy múa; skating=trượt patin; football=bóng đá; badminton=cầu lông; music=âm nhạc",
 """What's your hobby? - I like ___. (bơi lội)|swimming|swim|swims|swam
My hobby ___ painting.|is|are|am|do
I like ___ football.|playing|play|plays|played
Do you like singing? - Yes, I ___.|do|am|is|are
Does she like dancing? - Yes, she ___.|does|do|is|am
He ___ reading books.|likes|like|liking|liked""",
 """Sở thích của bạn là gì?|What's your hobby?
Mình thích bơi lội.|I like swimming.
Bạn có thích vẽ tranh không?|Do you like painting?
Bố mình thích nấu ăn.|My father likes cooking.
Chúng mình thích chơi cầu lông.|We like playing badminton."""),
("Unit 6: Our school",
 "school=trường học; library=thư viện; playground=sân chơi; gym=phòng thể dục; computer room=phòng máy tính; music room=phòng nhạc; art room=phòng mĩ thuật; canteen=căng tin; classroom=lớp học; floor=tầng; big=to; beautiful=đẹp",
 """Where is the library? - It's on the first ___.|floor|desk|bag|pen
This is our ___. (trường học)|school|house|garden|farm
Is your school big? - Yes, it ___.|is|are|am|do
We have lunch in the ___.|canteen|library|gym|art room
We draw pictures in the ___.|art room|gym|canteen|library
We play football in the ___.|playground|library|classroom|canteen""",
 """Đây là trường của mình.|This is my school.
Trường mình rất đẹp.|My school is very beautiful.
Thư viện ở tầng một.|The library is on the first floor.
Chúng mình chơi trên sân trường.|We play in the playground.
Chúng mình ăn trưa ở căng tin.|We have lunch in the canteen."""),
("Unit 7: Classroom",
 "book=quyển sách; pen=cái bút; pencil=bút chì; ruler=thước kẻ; rubber=cục tẩy; school bag=cặp sách; desk=bàn học; chair=ghế; board=bảng; door=cửa ra vào; window=cửa sổ; poster=áp phích",
 """May I ___ in, Miss?|come|comes|coming|came
May I sit ___, please?|down|up|in|on
Stand ___, please. (đứng lên)|up|down|out|in
Open your ___.|book|name|hello|friend
Close the ___, please. (cửa)|door|hello|name|friend
Is this your pen? - Yes, ___.|it is|it isn't|I am|I do""",
 """Em có thể vào lớp không ạ?|May I come in?
Em có thể ngồi xuống không ạ?|May I sit down?
Mở sách ra.|Open your book.
Hãy đứng lên.|Stand up, please.
Đây là bút của bạn à?|Is this your pen?"""),
("Unit 8: Toys and colours",
 "doll=búp bê; ball=quả bóng; kite=con diều; robot=người máy; car=ô tô; teddy bear=gấu bông; yo-yo=con quay yo-yo; train=tàu hỏa; plane=máy bay; toy=đồ chơi; colour=màu sắc; many=nhiều",
 """I have a ___. (quả bóng)|ball|doll|kite|car
What colour is your car? - It's ___.|red|big|nice|new
How many dolls do you have? - I have ___ dolls.|two|a|the|it
Do you have a robot? - No, I ___.|don't|am not|isn't|can't
There ___ three balls.|are|is|am|be
There ___ a kite.|is|are|am|be""",
 """Mình có một con búp bê.|I have a doll.
Bạn có bao nhiêu quả bóng?|How many balls do you have?
Mình có ba quả bóng.|I have three balls.
Ô tô của bạn màu gì?|What colour is your car?
Mình thích chơi với gấu bông.|I like playing with my teddy bear."""),
("Unit 9: Weather, time and places",
 "sunny=có nắng; rainy=có mưa; windy=có gió; cloudy=có mây; hot=nóng; cold=lạnh; park=công viên; beach=bãi biển; zoo=sở thú; house=ngôi nhà; garden=khu vườn; today=hôm nay",
 """What's the weather like? - It's ___. (có nắng)|sunny|rainy|snowy|cold
It's ___ today. (lạnh)|cold|hot|sunny|rainy
Let's go to the ___.|park|name|colour|book
Where are you? - I'm at the ___.|beach|doll|pen|kite
Is it hot? - Yes, it ___.|is|am|are|do
Is it rainy? - No, it ___.|isn't|aren't|am not|doesn't""",
 """Hôm nay trời nắng.|It's sunny today.
Hôm nay trời không mưa.|It isn't rainy today.
Chúng mình đi công viên nhé.|Let's go to the park.
Mình ở bãi biển.|I'm at the beach.
Trời lạnh quá.|It's very cold."""),
("Unit 10: Food, drinks and animals",
 "bread=bánh mì; rice=cơm; milk=sữa; water=nước; juice=nước ép; chicken=thịt gà; fish=cá; apple=quả táo; banana=quả chuối; cat=con mèo; dog=con chó; bird=con chim",
 """I'm thirsty. I'd like some ___.|water|bread|rice|chicken
I'm hungry. I'd like some ___.|bread|water|milk|juice
Do you like fish? - Yes, I ___.|do|am|is|are
I have a ___. (con mèo)|cat|catch|cut|cap
The dog ___ big.|is|are|am|be
Two ___ are in the garden. (con chim)|birds|bird|a bird|birdes""",
 """Mình đói. Mình muốn ăn chút bánh mì.|I'm hungry. I'd like some bread.
Mình khát. Mình muốn uống nước.|I'm thirsty. I'd like some water.
Bạn thích cá không?|Do you like fish?
Con mèo của mình rất dễ thương.|My cat is very cute.
Con chó kia rất to.|That dog is very big."""),
]
CHU_DE = make(U)
