import os

WEBHOOK_DOMAIN=DOMAIN = "https://www.manifestservices.in"


if os.environ.get('MODE') == 'production':
    pass
else:
    pass

TESTIMONIALS=[
                {'content':'Manifest services have helped us to list our products neatly in our website. This has helped me to explain the product to customers.',
                 'author':'KV Business solutions'},
                {'content':'We are very grateful to Manifest Services for delivering our eCommerce website with SEO. We are getting online traffic of 10k visiors per month. We have good increase in sales with brand popularity.',
                 'author':'Used Books Factory'},
                {'content':'We sold our medical eqipments with ease after taking this service. Best part is the shipment integration where they provided a merchant who can accept Cash on Delivery.',
                 'author':'Osmania medical house'},
                {'content':'I was able to convey all my course details and announcements throuh the website which Manifest services created. It has saved my time a lot.',
                 'author':'TRS Mathematics academy'},
                
                ]


WELCOME_SUBJECT = "Welcome to Used Books Factory"

OFFICIAL_PHONE = "+91 86681 45559"

OFFICIAL_MAIL = "info@manifestservices.in"

OFFICIAL_ADDRESS = "NO 33, ARUMUGAM NAGAR, FIRST STREET, MUGALIVAKKAM, CHENNAI, TAMIL NADU"

ORDER_CONFIRMATION_SUBJECT = "THANK YOU FOR YOUR ORDER"

ORDER_INPROGRESS_SUBJECT = "YOUR ORDER IS IN PROGRESS"

ORDER_FAILURE_SUBJECT = "YOUR ORDER HAS FAILED"

ORDER_TRACKING_SUBJECT = "YOUR ORDER IS DISPATCHED"

ORDER_DELIVERED_SUBJECT = "YOUR ORDER IS DELIVERED"

ORDER_DISPATCH_ALERT_SUBJECT = "ALERT! ALERT! ORDERS TO BE DISPATCHED"

ORDER_SELLER_SUBJECT = "YOU RECEIVED AN ORDER"

ORDER_FAILURE_BODY = "Unfortunately, your order with us has failed. Either you have not proceeded with payment within 15 minutes, or an internal error would have occurred. Any amount deducted, would be refunded back within 7 working days"

CONTACTUS_BODY = "Thank you for contacting us. We shall get back to you shortly. Feel free to reply to this mail or contact us on phone (+91 8668145559)"

WORK_SUBJECT = "Work assigned from UsedBooksFactory"

BOOK_AVAILABLE_SUBJECT = "Book Available in Stock"

REFUND_REQUEST_SUBJECT = "Request for Refund approval"

REFUND_INITIATED_SUBJECT = "Refund initated for order"

STAFF_MAIL_1 = "vino.kvvs@gmail.com"

STAFF_MAIL_2 = "nimisha49@gmail.com"

STAFF_MAIL_3 = "vasanthg271998@gmail.com"

CALL_CENTRE_STAFF_1 = "vineela.inri@gmail.com"

MAIL_LIST = [OFFICIAL_MAIL, STAFF_MAIL_1, STAFF_MAIL_2]

DEFAULT_IMAGE = 'images/default_image.jpg'

DTDC_TRACKING = 'http://www.dtdc.in/tracking/tracking_results_detail.asp'

GOOGLE_REVIEW_LINK = "https://search.google.com/local/writereview?placeid=ChIJ-0wddsVgUjoRmZLnC9cfOfc"

CUSTOMER_WISHLIST_EXCEL_LINK = "https://docs.google.com/spreadsheets/d/18CKJevL9bCogsxafEtnJRfO62R34tve_ngrlq3MJMts/edit?usp=sharing"
