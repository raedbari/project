# مقدمة المشروع

في عالم تطوير البرمجيات الحديث، أصبح من المهم بناء تطبيقات مرنة وسهلة النشر والإدارة. استخدام Docker أصبح شائعًا لأنه يسمح بتشغيل البرامج في حاويات مستقلة عن النظام الأساسي، مما يسهل التشغيل على أي جهاز.

هذا المشروع عبارة عن تطبيق ويب بسيط باستخدام Flask (إطار عمل بلغة Python) يتصل بقاعدة بيانات MySQL، وكل ذلك يتم تشغيله عبر Docker باستخدام docker-compose. الهدف هو بناء بيئة متكاملة لتطبيق ديناميكي يمكن نقله وتشغيله بسهولة على أي جهاز.

# ما هو المشروع 

:اسم المشروع
مشروع "Flask with MySQL using Docker"

وصف مختصر:
هو تطبيق ويب مصغر يُظهر كيفية إنشاء API بسيطة باستخدام Flask يمكنها:

عرض بيانات من قاعدة بيانات MySQL.

إضافة بيانات جديدة من خلال واجهة API.

كل جزء من التطبيق (Flask و MySQL) يتم تشغيله داخل حاوية Docker مستقلة ويتم ربطهما سويًا باستخدام Docker Compose.

وظائف المشروع الأساسية:
تشغيل تطبيق Flask في حاوية مستقلة.

تشغيل MySQL مع قاعدة بيانات تلقائية يتم إنشاؤها عبر ملف init.sql.

إنشاء API:

عرض البيانات (GET /)

إدخال بيانات (POST /add)

توصيل التطبيق بقاعدة البيانات داخل شبكة Docker خاصة.

سهولة التشغيل عبر أمر واحد فقط:
docker-compose up --build
واطفائه ب امر واحد 
docker compose down 
لكن قبل هذا الامر يجب عليك الضغط على ctrl+c لكي تخرج من وضع running لانك بعد كتابة الامر docker-compose up --build تدخل الى التطبيق لأطفاء التطبيق اظغط ctrl+c ثم docker compose down  اذا احببت تعديل الرساله الموجوده في mysql


1. docker-compose.yml
الوظيفة: هذا الملف مسؤول عن تشغيل الخدمات المختلفة مثل تطبيق Flask و MySQL في حاويات Docker مستقلة ولكنها متصلة ببعضها عبر شبكة خاصة.

ما الذي يفعله؟:

يقوم بتعريف الخدمة الخاصة بـ Flask والخدمة الخاصة





شرح الملفات:

1. docker-compose.yml
الوظيفة: الملف المسؤول عن تشغيل الخدمات في حاويات مستقلة. يقوم بتشغيل كل من تطبيق Flask و MySQL باستخدام Docker و docker-compose.


المحتوى:

تعريف حاويتين:

حاوية لتطبيق Flask (web).

حاوية لقاعدة البيانات MySQL (db).

ربط الحاويتين معًا عبر شبكة Docker الخاصة لضمان تواصلهما.


2. db/init.sql
الوظيفة: يحتوي على سكربت SQL يتم تنفيذه أول مرة عند تشغيل قاعدة البيانات.

المحتوى:

إنشاء قاعدة بيانات وجداولها.

إدخال بيانات مبدئية في قاعدة البيانات.

الاستخدام: يتم تنفيذ السكربت تلقائيًا عند بدء تشغيل حاوية MySQL لأول مرة.


3. app/Dockerfile
الوظيفة: يُستخدم لبناء صورة Docker مخصصة لتطبيق Flask.

المحتوى:

تثبيت Python وتحديث الحزم اللازمة.

نسخ ملفات المشروع داخل الحاوية.

تشغيل تطبيق Flask (app.py).

الاستخدام: عند تشغيل الحاوية، يقوم Docker ببناء الصورة من هذا الملف وتشغيل التطبيق داخل بيئة معزولة.


4. app/requirements.txt
الوظيفة: يحتوي على قائمة المكتبات التي يحتاجها تطبيق Flask.

المحتوى:

يحدد المكتبات الأساسية مثل flask و mysql-connector-python وغيرها.

الاستخدام: يُستخدم لتثبيت المكتبات المطلوبة عبر الأمر pip install -r requirements.txt.


5. app/app.py
الوظيفة: الكود الأساسي لتطبيق Flask.

المحتوى:

إنشاء تطبيق Flask باستخدام Python.

الاتصال بـ قاعدة بيانات MySQL عبر Python.

تنفيذ استعلامات SQL لاسترجاع البيانات وعرضها في واجهة المستخدم.

الاستخدام: عند تشغيل التطبيق، يتم استرجاع الرسائل من قاعدة البيانات وعرضها في المتصفح عند زيارة الصفحة الرئيسية.
