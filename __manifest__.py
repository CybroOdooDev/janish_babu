{
    'name': "Capture Image Uplaod",
    'version': '16.0.1.0.0',
    'installable': True,
    'application': True,
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'depends': ['web', 'contacts'],
    'assets': {
        'web.assets_backend': [
            'capture_image_field/static/src/xml/image_upload.xml',
            'capture_image_field/static/src/js/image_upload.js',
            'capture_image_field/static/src/xml/camera_dialog.xml',
            'capture_image_field/static/src/js/camera_dialog.js'
        ]
    },

}
