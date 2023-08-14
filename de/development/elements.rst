.. _development_elements_de:

Elemente verstehen
##################

*Anmerkung*: Dieser Guide wird überarbeitet. Wir werden eine neue Dokumentation im Contributing Guide für Entwickler bereitstellen, der sich im Git-Repository befindet:

`https://github.com/mapbender/mapbender-starter/blob/release/3.0.6/CONTRIBUTING.md#elements <https://github.com/mapbender/mapbender-starter/blob/release/3.0.6/CONTRIBUTING.md#elements>`_.


Bereiche der Elemente
**********************

PHP Class
+++++++++

TODO


Twig Template
+++++++++++++

Jedes Element benötigt ein HTML-Element. In den meisten Fällen kann das ein DIV-Element sein, aber es kann auch komplexer sein.

Für Mapbender wird Twig verwendet. Eine einfache Twig-Vorlage für ein Element kann wie folgt aussehen:

.. code-block:: html+jinja

    <div id="{{ id }}" class="mb-element mb-element-myclass"></div>

Mehrere Angaben müssen gesetzt werden: 

* id (wird von Mapbender generiert)
* allgemeine mb-element-Klasse 
* spezielle Klasse für das Element

JavaScript Widgets
++++++++++++++++++

Element Widgets werden unter Verwendung der jQuery UI `widget factory <https://jqueryui.pbworks.com/w/page/12138135/Widget%20factory>`_ erzeugt.
Dies gewährleistet eine einheitliche Struktur für die Widget-Entwicklung und bietet:

* voreingestellte Optionen. 
* Konstruktoren und Dekonstruktoren (optional)
* private und öffentliche Methoden.

Das grundlegende Gerüst sieht folgendermaßen aus:

.. code-block:: js

    (function($) {

    // Das ist die Widget Factory. Es wird sowohl die Widget-Klasse "mbMyClass" im jQuery-Objekt als auch eine 
    //  "mbMyClass" Object im "mapbender"-Namensraum im jQuery-Object  erzeugt (sie werden beide unterschiedlich verwendet). Verwenden Sie ein
    // "mb"-Präfix für Ihre Widget-Namen, damit existierende jQuery-Funktionen nicht überschrieben werden.
    $.widget('mapbender.mbMyClass', {
                 // Es werden voreingestellte Optionen angelegt, die in der Mapbender-Konfiguration überschrieben werden kann.
        //  Es wird später in die PHP-Klasse verschoben.
        // Auf das endgültige options-Objekt kann zugegriffen werden als "this.options". 

        options: {
            foo:    'bar',
            answer: 42
        },

        // Dieses Attribut ist privat für Ihr Widget.
        var1: null,

        // Der Konstruktor wird bei der Widget-Initialisierung aufgerufen.
        _create: function() {
            // Hier wird alles für das Setup angelegt, beispielsweise für das Event Handling 
            this.element.bind('mbmyclassmagicdone', $.proxy(this._onMagicDone, this));
            this.element.bind('click', $.proxy(this._clickCallback, this));
        },

        // Der Destruktor, wird in diesem Beispiel über jQuery geliefert.
        destroy: $.noop,

        // Öffentliche Funktion, sind beispielsweise über "$('#element-13').mbMyClass('methodA', parameterA, parameterB)" abrufbar 
        methodA: function(parameterA, parameterB) {
            this._methodB(parameterA);
        },

        //  Private Funktion, sind nur innerhalb des Widget abrufbar
        _methodB: function(parameterA) {
            // Das ausgelöste Signal wird genannt "mbmyclassmagicdone" (kleingeschrieben) 
            this._trigger('magicdone');
        },

        _onMagicDone: function() {
            alert("Oh, magic!");
        },

        _clickCallback: function(event) {
            var target = $(event.target);
            var id = target.attr('id');
            // ...
        }

    });

    })(jQuery);

Für das Event Handling wird jQuery.proxy verwendet, um sicherzustellen, dass ein der Callback im richtigen Kontext gewährleistet wird:


.. code-block:: js

    // ...

    this.element.click($.proxy(this._clickCallback, this));

    // ...

In diesem Fall ist "this" innerhalb der clickCallback Methode das This, das als der zweite Parameter übergeben wird (in der Regel die Widget Instanz) und nicht das HTML-Element, das das Event angestoßen hat.

Kommunikation zwischen Elementen
********************************

Es gibt eine aktive und passive Kommunikation zwischen den Widgets. Die aktive Kommunikation, wird genutzt, um eine öffentliche Methode eines anderen Widget abzurufen. Dazu selektieren Sie das HTML-Element des Widgets mit jQuery und rufen die Methode folgendermaßen auf:

.. code-block:: js

    var otherElement = $('#element-13').mbMyClass('methodA', parameterA, parameterB);

Dies ist eine Standard-jQuery UI Syntax und selbsterklärend. Es ist die Frage, wie Sie die anderen HTML-Elemente erkennen? Um ein Element zu selektieren, wird bevorzugt die ID verwendet. Diese ID's werden jedoch zur Laufzeit von Mapbender generiert, wenn die Anwendung startet, so dass Sie nicht davon ausgehen können, dass die ID immer gleich ist. Glücklicherweise können Sie in der Konfiguration eine Element-ID als eine Target-Option für ein anderes Element übergeben. Diese wird mit der Laufzeit-ID des Target-Elements des HTML-Element überschrieben, so dass Sie in Ihrem Widget-Code auf die richtige ID "this.options.target" zugreifen können. 

.. code-block:: js

    $('#' + this.options.target).mbMyClass('methodA', parameterA, parameterB);

Die passive Kommunikation wird verwendet, um Ereignisse anderer Targets anzumelden. Sie müssen das HTML-Element kennen und können nun dem anderen Widget lauschen, um ihr Widget abzurufen. Dieses wird mit Standard-jQuery-Events vorgenommen:

Wenn Sie die  "_trigger"-Methode mit jQuery UI Widget Factory bereitstellen ...
