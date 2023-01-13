# -*- coding: utf-8 -*-
{
    'name': "Advanced Rest Api",

    'summary': """
        Advanced REST API for Odoo is a module that allows users to access Odoo data and functionality through web services using the RESTful protocol""",

    'description': """
Advanced REST API for Odoo is a powerful module that enables developers to access Odoo data and functionality through web services using the RESTful protocol. This allows for seamless integration with other systems, automation of tasks, and the building of custom applications that can interact with Odoo. The module provides a user-friendly interface for interacting with the API and allows for easy customization of the returned data.

The RESTful API allows developers to access data stored in Odoo, such as customer information, sales data, and inventory levels, as well as perform actions like creating new records, updating existing ones, and deleting data. The API can also be used to trigger workflows, such as generating invoices or creating new sales orders.

The module also provides a powerful set of tools for customizing the returned data. This includes the ability to select specific fields to return, filter data based on certain criteria, and even perform calculations on the returned data. Additionally, the API can be easily extended to include custom models and fields, allowing for the integration of data from other systems.

Overall, Advanced REST API for Odoo is a valuable tool for developers looking to integrate Odoo with other systems or build custom applications that interact with Odoo data. It provides a comprehensive and easy-to-use interface for interacting with Odoo through web services, and offers powerful customization options to tailor the returned data to specific needs.
        REST API
    Odoo Integration
    Web Services
    Data Access
    Workflow Automation
    Custom Applications
    Customer Information
    Sales Data
    Inventory Levels
    Record Creation
    Record Updating
    Record Deletion
    Data Filtering
    Data Calculation
    Custom Models
    Custom Fields
    System Integration
    Data Accessibility
    API Customization
    Invoice Generation
    Sales Order Creation
    Data Extensibility
    Data Consistency
    User-friendly Interface
    Data Security
    Easy Customization
    Workflow Management
    Data Management
    Cloud Integration
    Automated Tasks
    Data Analysis
    Business Intelligence
    Real-time Data
    Data Visualization
    Multi-system Integration
    Mobile Application
    Web Application
    Business Automation
    Data Synchronization
    Advanced Functionality
    Intégration Odoo
     Services Web
     Accès aux données
     Automatisation du flux de travail
     Demandes personnalisées
     Informations client
     Données de vente
     Les niveaux d'inventaire
     Création d'enregistrement
     Mise à jour des enregistrements
     Suppression d'enregistrement
     Filtrage des données
     Calcul des données
     Modèles personnalisés
     Les champs personnalisés
     Systeme d'intégration
     Accessibilité des données
     Personnalisation de l'API
     Génération de facture
     Création de commande client
     Extensibilité des données
     La cohérence des données
     Interface conviviale
     Sécurité des données
     Personnalisation facile
     Gestion des flux de travail
     Gestion de données
     Intégration infonuagique
     Tâches automatisées
     L'analyse des données
     L'intelligence d'entreprise
     Données en temps réel
     Visualisation de données
     Intégration multi-système
     Application mobile
     Application Web
     Automatisation des affaires
     Synchronisation des données
     Fonctionnalité avancée
       Integración Odoo
     Servicios web
     Acceso a los datos
     Automatización del flujo de trabajo
     Aplicaciones personalizadas
     Información al cliente
     Los datos de ventas
     Niveles de inventario
     Creación de registros
     Actualización de registros
     Eliminación de registros
     Filtrado de datos
     Cálculo de datos
     Modelos personalizados
     Campos Personalizados
     Integración de sistema
     Accesibilidad de datos
     Personalización de API
     Generación de facturas
     Creación de órdenes de venta
     Extensibilidad de datos
     Consistencia de los datos
     Interfaz amigable
     Seguridad de datos
     Fácil personalización
     Gestión de flujo de trabajo
     Gestión de datos
     Integración en la nube
     Tareas automatizadas
     Análisis de los datos
     Inteligencia de Negocio
     Datos en tiempo real
     Visualización de datos
     Integración multisistema
     Aplicación movil
     Aplicación web
     Automatización de Negocios
     Sincronización de datos
     Funcionalidad avanzada
   تكامل Odoo
     خدمات الويب
     الدخول الى البيانات
     أتمتة سير العمل
     تطبيقات مخصصة
     معلومات العميل
     بيانات مبيعات
     مستويات الخزين
     إنشاء سجل
     تحديث السجل
     حذف التسجيل
     تصفية البيانات
     حساب البيانات
     النماذج المخصصة
     الحقول المخصصة
     نظام التكامل
     الوصول إلى البيانات
     تخصيص API
     إنشاء الفاتورة
     إنشاء أوامر المبيعات
     إمكانية توسيع البيانات
     تناسق البيانات
     واجهة سهلة الاستخدام
     أمن البيانات
     سهولة التخصيص
     إدارة تتابع الأعمال
     إدارة البيانات
     تكامل السحابة
     المهام الآلية
     تحليل البيانات
     ذكاء الأعمال
     معلومات الوقت الحقيقي
     عرض مرئي للمعلومات
     تكامل متعدد الأنظمة
     تطبيق الهاتف المحمول
     تطبيق الويب
     أتمتة الأعمال
     تزامن البيانات
     وظائف متقدمة
    """,

    'author': "medconsultantweb@gmail.com",
    'category': 'Extra Tools',
    'price': 55,
    'currency': 'EUR',
    'version': '12.0.0.0',
    'depends': ['base'],
    "data": [
            "data/ir_config_param.xml",
            "security/ir.model.access.csv",
            "views/res_users.xml",
            ],

    'application': True,
    'license': 'OPL-1',
    'images': [
        'static/description/main.png',
    ],
}