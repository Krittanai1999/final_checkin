# final_checkin
finaltest

1.อัพเดต! ข้อมูลนักเรียนสามารถเพิ่มได้แล้ว

2.อัพเดต! ข้อมูลครูสามารถเพิ่มได้แล้ว

3.อัพเดต! ข้อมูลผู้ปกครองสามารถเพิ่มได้แล้ว


1.แก้ไข! ตัว model Student ส่วน parent_id, teacher_id

2.แก้ไข! model ที่มี user อยู่เป็น จาก one to one เป็น forienkey ใช้ตัว form จาก django


1.การ login! admin เป็นฝ่ายทะเบียน username : admin password : 1234

2.การ login! นักเรียน admin เวลาเพิ่มข้อมูลนักเรียน admin จะสร้าง user ให้อัตโนมัติพร้อมรหัสผ่าน 1234

3.การ login! ครู admin เวลาเพิ่มข้อมูลครู admin จะสร้าง user ให้อัตโนมัติพร้อมรหัสผ่าน 1234


1.เพิ่มเติม! ทั้ง 3 ข้อมูลสามารถกดแก้ไข ลบได้

2.เพิ่มเติม! หน้าหลักนักเรียนต่องแสดงข้อมูลเฉพาะนักเรียนแค่นั้น

3.เพิ่มเติม! ต้องมี validate พี่ TA แกล้งบอก เช่น ถ้าข้อมูลไหนใส่ int แล้วเราใส่เป็น char ก้ต้องเตือน (แต่ไว้แก้ไขหลังสุด เอาข้อมูลภาพรวมให้แสดงก่อน)


1.เป้าหมายต่อไป!!!!!!!   ทำส่วนของ course จาก form html ธรรมดาให้เป็น django form หรือ model form ตามที่จารย์บอกว่าให้มีอย่างน้อย 1


---UPDATE 7/4/63---

Update 7/4/63
เพิ่มไฟล์
-	Studentdetail.html เพื่อแสดงข้อมูลของนักเรียนได้
-	Parentdetail.html เพื่อแสดงข้อมูลของผู้ปกครองได้
-	
Index.html
-	ยังไม่สามารถแสดงผลของตัวเองได้
-
View.py
-	สามารถใช้ parent_update ได้แล้ว แต่ติดตรงที่ first_name, last_name ไม่แสดงผล
-	สามารถใช้ parent_delete ได้แล้ว
-	Student_update ยังใช้ไม่ได้ ติดตรงform
-	สามารถใช้ student_delete ได้แล้ว
-	teacher_update ได้แล้ว
-	teacher_delete ติด FK มั้ง student
-	def student_detail(request, student_id):
-	def parent_detail(request, parent_id):
-	ทั้งนักเรียนกับ ผปค แสดงข้อมูลได้แล้ว
-
Student_add.html
-	มีการแก้ไข name, id คือ tel, email, address โดยการตัด 1 ท้ายชื่อออกหมด
-
School/Urls.py เพิ่ม
- path('detail/student/<int:student_id>/', views.student_detail, name='student_detail'),
- path('detail/parent/<int:parent_id>/', views.parent_detail, name='parent_detail'),
-
-เหลือ couse update.delete


 
