from tacore import make
U = [
("Unit 1: Hello",
 "hello=xin chào; goodbye=tạm biệt; hi=chào; bye=chào tạm biệt; name=tên; I=tôi; my=của tôi; friend=bạn; good morning=chào buổi sáng; good afternoon=chào buổi chiều; good night=chúc ngủ ngon; thank you=cảm ơn",
 """___, I'm Mai. (Xin chào)|Hello|Goodbye|Thank you|Sorry
What's your ___? - My name is Nam.|name|friend|bye|class
Gặp bạn buổi sáng, em nói: ___.|Good morning|Good night|Goodbye|Sorry
Trước khi đi ngủ, em nói: ___.|Good night|Good morning|Hello|Thank you
Khi tạm biệt bạn, em nói: ___.|Goodbye|Hello|Hi|Good morning
___ you! (Em cảm ơn cô)|Thank|Hello|Bye|Sit""",
 """Xin chào, mình là Lan.|Hello, I'm Lan.
Tên mình là Nam.|My name is Nam.
Tạm biệt các bạn.|Goodbye, friends.
Cảm ơn bạn.|Thank you.
Chào buổi sáng, cô ơi.|Good morning, teacher."""),
("Unit 2: In the classroom",
 "book=quyển sách; pen=cái bút; pencil=bút chì; ruler=thước kẻ; bag=cặp sách; desk=bàn học; chair=cái ghế; board=cái bảng; eraser=cục tẩy; teacher=giáo viên; student=học sinh; classroom=lớp học",
 """This is a ___. (cái bút chì)|pencil|ruler|bag|desk
It's a ___. (quyển sách)|book|chair|pen|board
Stand ___, please.|up|down|desk|book
Sit ___, please.|down|up|pen|bag
Open your ___.|book|name|hello|bye
Close your ___.|book|hi|good|friend""",
 """Đây là quyển sách của mình.|This is my book.
Đây là cái bút.|This is a pen.
Hãy đứng lên.|Stand up, please.
Hãy ngồi xuống.|Sit down, please.
Mở sách ra.|Open your book."""),
("Unit 3: Colours",
 "red=màu đỏ; blue=màu xanh dương; green=màu xanh lá; yellow=màu vàng; orange=màu cam; pink=màu hồng; purple=màu tím; black=màu đen; white=màu trắng; brown=màu nâu; colour=màu sắc; crayon=bút sáp màu",
 """What colour is it? - It's ___. (màu đỏ)|red|blue|green|pink
Quả chuối có màu ___.|yellow|blue|black|purple
Bầu trời có màu ___.|blue|brown|yellow|red
Lá cây có màu ___.|green|red|pink|white
My bag is ___. (màu đen)|black|white|orange|purple
Quả cam có màu ___.|orange|blue|green|black""",
 """Nó màu đỏ.|It's red.
Cặp của mình màu xanh dương.|My bag is blue.
Bút chì này màu vàng.|This pencil is yellow.
Bạn thích màu gì?|What colour do you like?
Mình thích màu hồng.|I like pink."""),
("Unit 4: My family",
 "father=bố; mother=mẹ; brother=anh/em trai; sister=chị/em gái; grandmother=bà; grandfather=ông; baby=em bé; family=gia đình; mum=mẹ; dad=bố; aunt=cô/dì; uncle=chú/bác",
 """This is my ___. (mẹ)|mother|father|brother|uncle
This is my ___. (bố)|father|mother|sister|aunt
He is my ___. (anh/em trai)|brother|sister|mother|baby
She is my ___. (chị/em gái)|sister|brother|father|uncle
This is my ___. (bà)|grandmother|grandfather|baby|dad
This is my ___. (ông)|grandfather|grandmother|mum|sister""",
 """Đây là gia đình mình.|This is my family.
Đây là bố mình.|This is my father.
Đây là mẹ mình.|This is my mother.
Bà mình rất hiền.|My grandmother is kind.
Mình có một em gái.|I have a sister."""),
("Unit 5: Numbers",
 "one=một; two=hai; three=ba; four=bốn; five=năm; six=sáu; seven=bảy; eight=tám; nine=chín; ten=mười; number=con số; count=đếm",
 """1 + 1 = ___|two|three|four|five
2 + 2 = ___|four|three|five|six
5 + 1 = ___|six|four|seven|eight
10 - 1 = ___|nine|eight|ten|seven
Số 7 trong tiếng Anh là ___.|seven|six|eight|nine
How many pens? - ___ pens. (3)|Three|Two|Four|Ten""",
 """Mình có hai quyển sách.|I have two books.
Có năm cái bút.|There are five pens.
Mình lên mười tuổi.|I am ten years old.
Đếm từ một đến mười.|Count from one to ten.
Có ba con mèo.|There are three cats."""),
("Unit 6: Toys",
 "ball=quả bóng; doll=búp bê; kite=con diều; car=ô tô; robot=người máy; teddy bear=gấu bông; bike=xe đạp; train=tàu hỏa; plane=máy bay; boat=thuyền; puzzle=trò ghép hình; toy=đồ chơi",
 """I have a ___. (quả bóng)|ball|doll|kite|car
Do you have a doll? - Yes, I ___.|do|am|is|can
Do you have a kite? - No, I ___.|don't|am not|isn't|can't
This is my ___. (gấu bông)|teddy bear|robot|train|ball
I like ___. (ô tô)|cars|bag|ruler|eraser
Con diều bay trên ___. (trời)|sky|desk|bag|board""",
 """Mình có một quả bóng.|I have a ball.
Đây là con búp bê của mình.|This is my doll.
Bạn có diều không?|Do you have a kite?
Mình thích chơi ô tô.|I like playing with cars.
Mình có một chiếc xe đạp.|I have a bike."""),
("Unit 7: Animals",
 "cat=con mèo; dog=con chó; bird=con chim; fish=con cá; rabbit=con thỏ; duck=con vịt; chicken=con gà; pig=con lợn; cow=con bò; horse=con ngựa; elephant=con voi; monkey=con khỉ",
 """This is a ___. (con mèo)|cat|dog|bird|fish
It's a ___. (con chó)|dog|cat|duck|pig
A ___ can fly. (chim)|bird|fish|pig|cow
A ___ can swim. (cá)|fish|bird|dog|cat
I like ___. (con thỏ)|rabbits|ruler|pencil|book
A ___ says "moo". (bò)|cow|duck|cat|pig""",
 """Mình có một con mèo.|I have a cat.
Con chó của mình rất to.|My dog is big.
Con chim biết bay.|The bird can fly.
Con cá bơi trong nước.|The fish swims in the water.
Mình thích con voi.|I like elephants."""),
("Unit 8: My body",
 "head=đầu; eye=mắt; ear=tai; nose=mũi; mouth=miệng; hand=bàn tay; arm=cánh tay; leg=chân; foot=bàn chân; face=khuôn mặt; hair=tóc; body=cơ thể",
 """I see with my ___. (mắt)|eyes|ears|nose|mouth
I hear with my ___. (tai)|ears|eyes|hands|legs
I smell with my ___. (mũi)|nose|mouth|ears|hands
I eat with my ___. (miệng)|mouth|eyes|nose|ears
I walk with my ___. (chân)|legs|arms|eyes|ears
Touch your ___. (đầu)|head|book|desk|pen""",
 """Đây là mắt của mình.|These are my eyes.
Chạm vào mũi của bạn.|Touch your nose.
Mình có hai bàn tay.|I have two hands.
Mình có hai cái tai.|I have two ears.
Chỉ vào miệng của bạn.|Point to your mouth."""),
("Unit 9: Food and drinks",
 "apple=quả táo; banana=quả chuối; milk=sữa; water=nước; bread=bánh mì; rice=cơm; egg=quả trứng; cake=bánh ngọt; juice=nước ép; fish=cá; chicken=thịt gà; orange=quả cam",
 """I like ___. (quả táo)|apples|rulers|books|bags
I'm thirsty. I want some ___.|water|bread|rice|cake
I'm hungry. I want some ___.|rice|water|milk|juice
I drink ___. (sữa)|milk|bread|egg|cake
I eat ___. (bánh mì)|bread|water|milk|juice
Do you like bananas? - Yes, I ___.|do|am|is|can""",
 """Mình thích táo.|I like apples.
Mình muốn uống nước.|I want some water.
Mình đói.|I'm hungry.
Mình khát.|I'm thirsty.
Bạn thích bánh không?|Do you like cake?"""),
("Unit 10: Weather and action words",
 "sunny=có nắng; rainy=có mưa; cloudy=có mây; windy=có gió; hot=nóng; cold=lạnh; run=chạy; jump=nhảy; walk=đi bộ; swim=bơi; sing=hát; dance=múa",
 """It's ___ today. (có nắng)|sunny|rainy|cold|windy
It's ___. Take an umbrella. (mưa)|rainy|sunny|hot|windy
I can ___. (bơi)|swim|book|pen|desk
I can ___. (hát)|sing|ruler|bag|chair
Can you jump? - Yes, I ___.|can|am|do|is
Can you fly? - No, I ___.|can't|am|do|is""",
 """Hôm nay trời nắng.|It's sunny today.
Hôm nay trời mưa.|It's rainy today.
Mình biết nhảy.|I can jump.
Mình biết bơi.|I can swim.
Mình không biết bay.|I can't fly."""),
]
CHU_DE = make(U)
