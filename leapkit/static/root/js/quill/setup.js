(function() {
  var editor;

  editor = new Quill('.advanced-wrapper .editor-container', {
    modules: {
      'authorship': {
        enabled: true
      },
      'toolbar': {
        container: '.advanced-wrapper .toolbar-container'
      },
      'link-tooltip': true,
      'image-tooltip': true,
      'multi-cursor': true
    },
    theme: 'snow'
  });

  editor.on('text-change', function(delta, source) {
        var body = document.getElementById('hiddenBody');
        body.value = editor.getText();
  });


}).call(this);
