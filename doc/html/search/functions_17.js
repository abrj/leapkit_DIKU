var searchData=
[
  ['was_5fasked_5frecently',['was_asked_recently',['../classqueries_1_1models_1_1_user_question.html#a177afa95b1069ce137e78fd8fd8bed5a',1,'queries::models::UserQuestion']]],
  ['widget',['widget',['../root_2static_2root_2js_2bootstrap_2jquery-ui-1_810_84_8custom_8min_8js.html#a7045c273995cc5d25194ae884bacf39c',1,'widget(&quot;ui.mouse&quot;,{version:&quot;1.10.4&quot;, options:{cancel:&quot;input,textarea,button,select,option&quot;, distance:1, delay:0}, _mouseInit:function(){var e=this;this.element.bind(&quot;mousedown.&quot;+this.widgetName, function(t){return e._mouseDown(t)}).bind(&quot;click.&quot;+this.widgetName, function(i){return!0===t.data(i.target, e.widgetName+&quot;.preventClickEvent&quot;)?(t.removeData(i.target, e.widgetName+&quot;.preventClickEvent&quot;), i.stopImmediatePropagation(),!1):undefined}), this.started=!1}, _mouseDestroy:function(){this.element.unbind(&quot;.&quot;+this.widgetName), this._mouseMoveDelegate &amp;&amp;t(document).unbind(&quot;mousemove.&quot;+this.widgetName, this._mouseMoveDelegate).unbind(&quot;mouseup.&quot;+this.widgetName, this._mouseUpDelegate)}, _mouseDown:function(i){if(!e){this._mouseStarted &amp;&amp;this._mouseUp(i), this._mouseDownEvent=i;var s=this, n=1===i.which, a=&quot;string&quot;==typeof this.options.cancel &amp;&amp;i.target.nodeName?t(i.target).closest(this.options.cancel).length:!1;return n &amp;&amp;!a &amp;&amp;this._mouseCapture(i)?(this.mouseDelayMet=!this.options.delay, this.mouseDelayMet||(this._mouseDelayTimer=setTimeout(function(){s.mouseDelayMet=!0}, this.options.delay)), this._mouseDistanceMet(i)&amp;&amp;this._mouseDelayMet(i)&amp;&amp;(this._mouseStarted=this._mouseStart(i)!==!1,!this._mouseStarted)?(i.preventDefault(),!0):(!0===t.data(i.target, this.widgetName+&quot;.preventClickEvent&quot;)&amp;&amp;t.removeData(i.target, this.widgetName+&quot;.preventClickEvent&quot;), this._mouseMoveDelegate=function(t){return s._mouseMove(t)}, this._mouseUpDelegate=function(t){return s._mouseUp(t)}, t(document).bind(&quot;mousemove.&quot;+this.widgetName, this._mouseMoveDelegate).bind(&quot;mouseup.&quot;+this.widgetName, this._mouseUpDelegate), i.preventDefault(), e=!0,!0)):!0}}, _mouseMove:function(e){return t.ui.ie &amp;&amp;(!document.documentMode||9 &gt;document.documentMode)&amp;&amp;!e.button?this._mouseUp(e):this._mouseStarted?(this._mouseDrag(e), e.preventDefault()):(this._mouseDistanceMet(e)&amp;&amp;this._mouseDelayMet(e)&amp;&amp;(this._mouseStarted=this._mouseStart(this._mouseDownEvent, e)!==!1, this._mouseStarted?this._mouseDrag(e):this._mouseUp(e)),!this._mouseStarted)}, _mouseUp:function(e){return t(document).unbind(&quot;mousemove.&quot;+this.widgetName, this._mouseMoveDelegate).unbind(&quot;mouseup.&quot;+this.widgetName, this._mouseUpDelegate), this._mouseStarted &amp;&amp;(this._mouseStarted=!1, e.target===this._mouseDownEvent.target &amp;&amp;t.data(e.target, this.widgetName+&quot;.preventClickEvent&quot;,!0), this._mouseStop(e)),!1}, _mouseDistanceMet:function(t){return Math.max(Math.abs(this._mouseDownEvent.pageX-t.pageX), Math.abs(this._mouseDownEvent.pageY-t.pageY))&gt;=this.options.distance}, _mouseDelayMet:function(){return this.mouseDelayMet}, _mouseStart:function(){}, _mouseDrag:function(){}, _mouseStop:function(){}, _mouseCapture:function(){return!0}})})(jQuery):&#160;jquery-ui-1.10.4.custom.min.js'],['../root_2static_2root_2js_2bootstrap_2jquery-ui-1_810_84_8custom_8min_8js.html#a583de2e05fddf3b81ff89a3332cffb0d',1,'widget(&quot;ui.slider&quot;, t.ui.mouse,{version:&quot;1.10.4&quot;, widgetEventPrefix:&quot;slide&quot;, options:{animate:!1, distance:0, max:100, min:0, orientation:&quot;horizontal&quot;, range:!1, step:1, value:0, values:null, change:null, slide:null, start:null, stop:null}, _create:function(){this._keySliding=!1, this._mouseSliding=!1, this._animateOff=!0, this._handleIndex=null, this._detectOrientation(), this._mouseInit(), this.element.addClass(&quot;ui-slider ui-slider-&quot;+this.orientation+&quot; ui-widget&quot;+&quot; ui-widget-content&quot;+&quot; ui-corner-all&quot;), this._refresh(), this._setOption(&quot;disabled&quot;, this.options.disabled), this._animateOff=!1}, _refresh:function(){this._createRange(), this._createHandles(), this._setupEvents(), this._refreshValue()}, _createHandles:function(){var e, i, s=this.options, n=this.element.find(&quot;.ui-slider-handle&quot;).addClass(&quot;ui-state-default ui-corner-all&quot;), a=&quot;&lt;a class=&apos;ui-slider-handle ui-state-default ui-corner-all&apos; href=&apos;#&apos;&gt;&lt;/a&gt;&quot;, o=[];for(i=s.values &amp;&amp;s.values.length||1, n.length &gt;i &amp;&amp;(n.slice(i).remove(), n=n.slice(0, i)), e=n.length;i &gt;e;e++) o.push(a);this.handles=n.add(t(o.join(&quot;&quot;)).appendTo(this.element)), this.handle=this.handles.eq(0), this.handles.each(function(e){t(this).data(&quot;ui-slider-handle-index&quot;, e)})}, _createRange:function(){var e=this.options, i=&quot;&quot;;e.range?(e.range===!0 &amp;&amp;(e.values?e.values.length &amp;&amp;2!==e.values.length?e.values=[e.values[0], e.values[0]]:t.isArray(e.values)&amp;&amp;(e.values=e.values.slice(0)):e.values=[this._valueMin(), this._valueMin()]), this.range &amp;&amp;this.range.length?this.range.removeClass(&quot;ui-slider-range-min ui-slider-range-max&quot;).css({left:&quot;&quot;, bottom:&quot;&quot;}):(this.range=t(&quot;&lt;div&gt;&lt;/div&gt;&quot;).appendTo(this.element), i=&quot;ui-slider-range ui-widget-header ui-corner-all&quot;), this.range.addClass(i+(&quot;min&quot;===e.range||&quot;max&quot;===e.range?&quot; ui-slider-range-&quot;+e.range:&quot;&quot;))):(this.range &amp;&amp;this.range.remove(), this.range=null)}, _setupEvents:function(){var t=this.handles.add(this.range).filter(&quot;a&quot;);this._off(t), this._on(t, this._handleEvents), this._hoverable(t), this._focusable(t)}, _destroy:function(){this.handles.remove(), this.range &amp;&amp;this.range.remove(), this.element.removeClass(&quot;ui-slider ui-slider-horizontal ui-slider-vertical ui-widget ui-widget-content ui-corner-all&quot;), this._mouseDestroy()}, _mouseCapture:function(e){var i, s, n, a, o, r, l, h, u=this, c=this.options;return c.disabled?!1:(this.elementSize={width:this.element.outerWidth(), height:this.element.outerHeight()}, this.elementOffset=this.element.offset(), i={x:e.pageX, y:e.pageY}, s=this._normValueFromMouse(i), n=this._valueMax()-this._valueMin()+1, this.handles.each(function(e){var i=Math.abs(s-u.values(e));(n &gt;i||n===i &amp;&amp;(e===u._lastChangedValue||u.values(e)===c.min))&amp;&amp;(n=i, a=t(this), o=e)}), r=this._start(e, o), r===!1?!1:(this._mouseSliding=!0, this._handleIndex=o, a.addClass(&quot;ui-state-active&quot;).focus(), l=a.offset(), h=!t(e.target).parents().addBack().is(&quot;.ui-slider-handle&quot;), this._clickOffset=h?{left:0, top:0}:{left:e.pageX-l.left-a.width()/2, top:e.pageY-l.top-a.height()/2-(parseInt(a.css(&quot;borderTopWidth&quot;), 10)||0)-(parseInt(a.css(&quot;borderBottomWidth&quot;), 10)||0)+(parseInt(a.css(&quot;marginTop&quot;), 10)||0)}, this.handles.hasClass(&quot;ui-state-hover&quot;)||this._slide(e, o, s), this._animateOff=!0,!0))}, _mouseStart:function(){return!0}, _mouseDrag:function(t){var e={x:t.pageX, y:t.pageY}, i=this._normValueFromMouse(e);return this._slide(t, this._handleIndex, i),!1}, _mouseStop:function(t){return this.handles.removeClass(&quot;ui-state-active&quot;), this._mouseSliding=!1, this._stop(t, this._handleIndex), this._change(t, this._handleIndex), this._handleIndex=null, this._clickOffset=null, this._animateOff=!1,!1}, _detectOrientation:function(){this.orientation=&quot;vertical&quot;===this.options.orientation?&quot;vertical&quot;:&quot;horizontal&quot;}, _normValueFromMouse:function(t){var e, i, s, n, a;return&quot;horizontal&quot;===this.orientation?(e=this.elementSize.width, i=t.x-this.elementOffset.left-(this._clickOffset?this._clickOffset.left:0)):(e=this.elementSize.height, i=t.y-this.elementOffset.top-(this._clickOffset?this._clickOffset.top:0)), s=i/e, s &gt;1 &amp;&amp;(s=1), 0 &gt;s &amp;&amp;(s=0),&quot;vertical&quot;===this.orientation &amp;&amp;(s=1-s), n=this._valueMax()-this._valueMin(), a=this._valueMin()+s *n, this._trimAlignValue(a)}, _start:function(t, e){var i={handle:this.handles[e], value:this.value()};return this.options.values &amp;&amp;this.options.values.length &amp;&amp;(i.value=this.values(e), i.values=this.values()), this._trigger(&quot;start&quot;, t, i)}, _slide:function(t, e, i){var s, n, a;this.options.values &amp;&amp;this.options.values.length?(s=this.values(e?0:1), 2===this.options.values.length &amp;&amp;this.options.range===!0 &amp;&amp;(0===e &amp;&amp;i &gt;s||1===e &amp;&amp;s &gt;i)&amp;&amp;(i=s), i!==this.values(e)&amp;&amp;(n=this.values(), n[e]=i, a=this._trigger(&quot;slide&quot;, t,{handle:this.handles[e], value:i, values:n}), s=this.values(e?0:1), a!==!1 &amp;&amp;this.values(e, i))):i!==this.value()&amp;&amp;(a=this._trigger(&quot;slide&quot;, t,{handle:this.handles[e], value:i}), a!==!1 &amp;&amp;this.value(i))}, _stop:function(t, e){var i={handle:this.handles[e], value:this.value()};this.options.values &amp;&amp;this.options.values.length &amp;&amp;(i.value=this.values(e), i.values=this.values()), this._trigger(&quot;stop&quot;, t, i)}, _change:function(t, e){if(!this._keySliding &amp;&amp;!this._mouseSliding){var i={handle:this.handles[e], value:this.value()};this.options.values &amp;&amp;this.options.values.length &amp;&amp;(i.value=this.values(e), i.values=this.values()), this._lastChangedValue=e, this._trigger(&quot;change&quot;, t, i)}}, value:function(t){return arguments.length?(this.options.value=this._trimAlignValue(t), this._refreshValue(), this._change(null, 0), undefined):this._value()}, values:function(e, i){var s, n, a;if(arguments.length &gt;1) return this.options.values[e]=this._trimAlignValue(i), this._refreshValue(), this._change(null, e), undefined;if(!arguments.length) return this._values();if(!t.isArray(arguments[0])) return this.options.values &amp;&amp;this.options.values.length?this._values(e):this.value();for(s=this.options.values, n=arguments[0], a=0;s.length &gt;a;a+=1) s[a]=this._trimAlignValue(n[a]), this._change(null, a);this._refreshValue()}, _setOption:function(e, i){var s, n=0;switch(&quot;range&quot;===e &amp;&amp;this.options.range===!0 &amp;&amp;(&quot;min&quot;===i?(this.options.value=this._values(0), this.options.values=null):&quot;max&quot;===i &amp;&amp;(this.options.value=this._values(this.options.values.length-1), this.options.values=null)), t.isArray(this.options.values)&amp;&amp;(n=this.options.values.length), t.Widget.prototype._setOption.apply(this, arguments), e){case&quot;orientation&quot;:this._detectOrientation(), this.element.removeClass(&quot;ui-slider-horizontal ui-slider-vertical&quot;).addClass(&quot;ui-slider-&quot;+this.orientation), this._refreshValue();break;case&quot;value&quot;:this._animateOff=!0, this._refreshValue(), this._change(null, 0), this._animateOff=!1;break;case&quot;values&quot;:for(this._animateOff=!0, this._refreshValue(), s=0;n &gt;s;s+=1) this._change(null, s);this._animateOff=!1;break;case&quot;min&quot;:case&quot;max&quot;:this._animateOff=!0, this._refreshValue(), this._animateOff=!1;break;case&quot;range&quot;:this._animateOff=!0, this._refresh(), this._animateOff=!1}}, _value:function(){var t=this.options.value;return t=this._trimAlignValue(t)}, _values:function(t){var e, i, s;if(arguments.length) return e=this.options.values[t], e=this._trimAlignValue(e);if(this.options.values &amp;&amp;this.options.values.length){for(i=this.options.values.slice(), s=0;i.length &gt;s;s+=1) i[s]=this._trimAlignValue(i[s]);return i}return[]}, _trimAlignValue:function(t){if(this._valueMin()&gt;=t) return this._valueMin();if(t &gt;=this._valueMax()) return this._valueMax();var e=this.options.step &gt;0?this.options.step:1, i=(t-this._valueMin())%e, s=t-i;return 2 *Math.abs(i)&gt;=e &amp;&amp;(s+=i &gt;0?e:-e), parseFloat(s.toFixed(5))}, _valueMin:function(){return this.options.min}, _valueMax:function(){return this.options.max}, _refreshValue:function(){var e, i, s, n, a, o=this.options.range, r=this.options, l=this, h=this._animateOff?!1:r.animate, u={};this.options.values &amp;&amp;this.options.values.length?this.handles.each(function(s){i=100 *((l.values(s)-l._valueMin())/(l._valueMax()-l._valueMin())), u[&quot;horizontal&quot;===l.orientation?&quot;left&quot;:&quot;bottom&quot;]=i+&quot;%&quot;, t(this).stop(1, 1)[h?&quot;animate&quot;:&quot;css&quot;](u, r.animate), l.options.range===!0 &amp;&amp;(&quot;horizontal&quot;===l.orientation?(0===s &amp;&amp;l.range.stop(1, 1)[h?&quot;animate&quot;:&quot;css&quot;]({left:i+&quot;%&quot;}, r.animate), 1===s &amp;&amp;l.range[h?&quot;animate&quot;:&quot;css&quot;]({width:i-e+&quot;%&quot;},{queue:!1, duration:r.animate})):(0===s &amp;&amp;l.range.stop(1, 1)[h?&quot;animate&quot;:&quot;css&quot;]({bottom:i+&quot;%&quot;}, r.animate), 1===s &amp;&amp;l.range[h?&quot;animate&quot;:&quot;css&quot;]({height:i-e+&quot;%&quot;},{queue:!1, duration:r.animate}))), e=i}):(s=this.value(), n=this._valueMin(), a=this._valueMax(), i=a!==n?100 *((s-n)/(a-n)):0, u[&quot;horizontal&quot;===this.orientation?&quot;left&quot;:&quot;bottom&quot;]=i+&quot;%&quot;, this.handle.stop(1, 1)[h?&quot;animate&quot;:&quot;css&quot;](u, r.animate),&quot;min&quot;===o &amp;&amp;&quot;horizontal&quot;===this.orientation &amp;&amp;this.range.stop(1, 1)[h?&quot;animate&quot;:&quot;css&quot;]({width:i+&quot;%&quot;}, r.animate),&quot;max&quot;===o &amp;&amp;&quot;horizontal&quot;===this.orientation &amp;&amp;this.range[h?&quot;animate&quot;:&quot;css&quot;]({width:100-i+&quot;%&quot;},{queue:!1, duration:r.animate}),&quot;min&quot;===o &amp;&amp;&quot;vertical&quot;===this.orientation &amp;&amp;this.range.stop(1, 1)[h?&quot;animate&quot;:&quot;css&quot;]({height:i+&quot;%&quot;}, r.animate),&quot;max&quot;===o &amp;&amp;&quot;vertical&quot;===this.orientation &amp;&amp;this.range[h?&quot;animate&quot;:&quot;css&quot;]({height:100-i+&quot;%&quot;},{queue:!1, duration:r.animate}))}, _handleEvents:{keydown:function(i){var s, n, a, o, r=t(i.target).data(&quot;ui-slider-handle-index&quot;);switch(i.keyCode){case t.ui.keyCode.HOME:case t.ui.keyCode.END:case t.ui.keyCode.PAGE_UP:case t.ui.keyCode.PAGE_DOWN:case t.ui.keyCode.UP:case t.ui.keyCode.RIGHT:case t.ui.keyCode.DOWN:case t.ui.keyCode.LEFT:if(i.preventDefault(),!this._keySliding &amp;&amp;(this._keySliding=!0, t(i.target).addClass(&quot;ui-state-active&quot;), s=this._start(i, r), s===!1)) return}switch(o=this.options.step, n=a=this.options.values &amp;&amp;this.options.values.length?this.values(r):this.value(), i.keyCode){case t.ui.keyCode.HOME:a=this._valueMin();break;case t.ui.keyCode.END:a=this._valueMax();break;case t.ui.keyCode.PAGE_UP:a=this._trimAlignValue(n+(this._valueMax()-this._valueMin())/e);break;case t.ui.keyCode.PAGE_DOWN:a=this._trimAlignValue(n-(this._valueMax()-this._valueMin())/e);break;case t.ui.keyCode.UP:case t.ui.keyCode.RIGHT:if(n===this._valueMax()) return;a=this._trimAlignValue(n+o);break;case t.ui.keyCode.DOWN:case t.ui.keyCode.LEFT:if(n===this._valueMin()) return;a=this._trimAlignValue(n-o)}this._slide(i, r, a)}, click:function(t){t.preventDefault()}, keyup:function(e){var i=t(e.target).data(&quot;ui-slider-handle-index&quot;);this._keySliding &amp;&amp;(this._keySliding=!1, this._stop(e, i), this._change(e, i), t(e.target).removeClass(&quot;ui-state-active&quot;))}}})})(jQuery):&#160;jquery-ui-1.10.4.custom.min.js'],['../root_2static_2root_2js_2jquery-ui_8custom_8min_8js.html#a175590539c18cdb8be1adc1c2cb681a5',1,'widget(&quot;ui.mouse&quot;,{version:&quot;1.10.3&quot;, options:{cancel:&quot;input,textarea,button,select,option&quot;, distance:1, delay:0}, _mouseInit:function(){var t=this;this.element.bind(&quot;mousedown.&quot;+this.widgetName, function(e){return t._mouseDown(e)}).bind(&quot;click.&quot;+this.widgetName, function(i){return!0===e.data(i.target, t.widgetName+&quot;.preventClickEvent&quot;)?(e.removeData(i.target, t.widgetName+&quot;.preventClickEvent&quot;), i.stopImmediatePropagation(),!1):undefined}), this.started=!1}, _mouseDestroy:function(){this.element.unbind(&quot;.&quot;+this.widgetName), this._mouseMoveDelegate &amp;&amp;e(document).unbind(&quot;mousemove.&quot;+this.widgetName, this._mouseMoveDelegate).unbind(&quot;mouseup.&quot;+this.widgetName, this._mouseUpDelegate)}, _mouseDown:function(i){if(!t){this._mouseStarted &amp;&amp;this._mouseUp(i), this._mouseDownEvent=i;var s=this, n=1===i.which, a=&quot;string&quot;==typeof this.options.cancel &amp;&amp;i.target.nodeName?e(i.target).closest(this.options.cancel).length:!1;return n &amp;&amp;!a &amp;&amp;this._mouseCapture(i)?(this.mouseDelayMet=!this.options.delay, this.mouseDelayMet||(this._mouseDelayTimer=setTimeout(function(){s.mouseDelayMet=!0}, this.options.delay)), this._mouseDistanceMet(i)&amp;&amp;this._mouseDelayMet(i)&amp;&amp;(this._mouseStarted=this._mouseStart(i)!==!1,!this._mouseStarted)?(i.preventDefault(),!0):(!0===e.data(i.target, this.widgetName+&quot;.preventClickEvent&quot;)&amp;&amp;e.removeData(i.target, this.widgetName+&quot;.preventClickEvent&quot;), this._mouseMoveDelegate=function(e){return s._mouseMove(e)}, this._mouseUpDelegate=function(e){return s._mouseUp(e)}, e(document).bind(&quot;mousemove.&quot;+this.widgetName, this._mouseMoveDelegate).bind(&quot;mouseup.&quot;+this.widgetName, this._mouseUpDelegate), i.preventDefault(), t=!0,!0)):!0}}, _mouseMove:function(t){return e.ui.ie &amp;&amp;(!document.documentMode||9 &gt;document.documentMode)&amp;&amp;!t.button?this._mouseUp(t):this._mouseStarted?(this._mouseDrag(t), t.preventDefault()):(this._mouseDistanceMet(t)&amp;&amp;this._mouseDelayMet(t)&amp;&amp;(this._mouseStarted=this._mouseStart(this._mouseDownEvent, t)!==!1, this._mouseStarted?this._mouseDrag(t):this._mouseUp(t)),!this._mouseStarted)}, _mouseUp:function(t){return e(document).unbind(&quot;mousemove.&quot;+this.widgetName, this._mouseMoveDelegate).unbind(&quot;mouseup.&quot;+this.widgetName, this._mouseUpDelegate), this._mouseStarted &amp;&amp;(this._mouseStarted=!1, t.target===this._mouseDownEvent.target &amp;&amp;e.data(t.target, this.widgetName+&quot;.preventClickEvent&quot;,!0), this._mouseStop(t)),!1}, _mouseDistanceMet:function(e){return Math.max(Math.abs(this._mouseDownEvent.pageX-e.pageX), Math.abs(this._mouseDownEvent.pageY-e.pageY))&gt;=this.options.distance}, _mouseDelayMet:function(){return this.mouseDelayMet}, _mouseStart:function(){}, _mouseDrag:function(){}, _mouseStop:function(){}, _mouseCapture:function(){return!0}})})(jQuery):&#160;jquery-ui.custom.min.js'],['../static_2root_2js_2bootstrap_2jquery-ui-1_810_84_8custom_8min_8js.html#a7045c273995cc5d25194ae884bacf39c',1,'widget(&quot;ui.mouse&quot;,{version:&quot;1.10.4&quot;, options:{cancel:&quot;input,textarea,button,select,option&quot;, distance:1, delay:0}, _mouseInit:function(){var e=this;this.element.bind(&quot;mousedown.&quot;+this.widgetName, function(t){return e._mouseDown(t)}).bind(&quot;click.&quot;+this.widgetName, function(i){return!0===t.data(i.target, e.widgetName+&quot;.preventClickEvent&quot;)?(t.removeData(i.target, e.widgetName+&quot;.preventClickEvent&quot;), i.stopImmediatePropagation(),!1):undefined}), this.started=!1}, _mouseDestroy:function(){this.element.unbind(&quot;.&quot;+this.widgetName), this._mouseMoveDelegate &amp;&amp;t(document).unbind(&quot;mousemove.&quot;+this.widgetName, this._mouseMoveDelegate).unbind(&quot;mouseup.&quot;+this.widgetName, this._mouseUpDelegate)}, _mouseDown:function(i){if(!e){this._mouseStarted &amp;&amp;this._mouseUp(i), this._mouseDownEvent=i;var s=this, n=1===i.which, a=&quot;string&quot;==typeof this.options.cancel &amp;&amp;i.target.nodeName?t(i.target).closest(this.options.cancel).length:!1;return n &amp;&amp;!a &amp;&amp;this._mouseCapture(i)?(this.mouseDelayMet=!this.options.delay, this.mouseDelayMet||(this._mouseDelayTimer=setTimeout(function(){s.mouseDelayMet=!0}, this.options.delay)), this._mouseDistanceMet(i)&amp;&amp;this._mouseDelayMet(i)&amp;&amp;(this._mouseStarted=this._mouseStart(i)!==!1,!this._mouseStarted)?(i.preventDefault(),!0):(!0===t.data(i.target, this.widgetName+&quot;.preventClickEvent&quot;)&amp;&amp;t.removeData(i.target, this.widgetName+&quot;.preventClickEvent&quot;), this._mouseMoveDelegate=function(t){return s._mouseMove(t)}, this._mouseUpDelegate=function(t){return s._mouseUp(t)}, t(document).bind(&quot;mousemove.&quot;+this.widgetName, this._mouseMoveDelegate).bind(&quot;mouseup.&quot;+this.widgetName, this._mouseUpDelegate), i.preventDefault(), e=!0,!0)):!0}}, _mouseMove:function(e){return t.ui.ie &amp;&amp;(!document.documentMode||9 &gt;document.documentMode)&amp;&amp;!e.button?this._mouseUp(e):this._mouseStarted?(this._mouseDrag(e), e.preventDefault()):(this._mouseDistanceMet(e)&amp;&amp;this._mouseDelayMet(e)&amp;&amp;(this._mouseStarted=this._mouseStart(this._mouseDownEvent, e)!==!1, this._mouseStarted?this._mouseDrag(e):this._mouseUp(e)),!this._mouseStarted)}, _mouseUp:function(e){return t(document).unbind(&quot;mousemove.&quot;+this.widgetName, this._mouseMoveDelegate).unbind(&quot;mouseup.&quot;+this.widgetName, this._mouseUpDelegate), this._mouseStarted &amp;&amp;(this._mouseStarted=!1, e.target===this._mouseDownEvent.target &amp;&amp;t.data(e.target, this.widgetName+&quot;.preventClickEvent&quot;,!0), this._mouseStop(e)),!1}, _mouseDistanceMet:function(t){return Math.max(Math.abs(this._mouseDownEvent.pageX-t.pageX), Math.abs(this._mouseDownEvent.pageY-t.pageY))&gt;=this.options.distance}, _mouseDelayMet:function(){return this.mouseDelayMet}, _mouseStart:function(){}, _mouseDrag:function(){}, _mouseStop:function(){}, _mouseCapture:function(){return!0}})})(jQuery):&#160;jquery-ui-1.10.4.custom.min.js'],['../static_2root_2js_2bootstrap_2jquery-ui-1_810_84_8custom_8min_8js.html#a583de2e05fddf3b81ff89a3332cffb0d',1,'widget(&quot;ui.slider&quot;, t.ui.mouse,{version:&quot;1.10.4&quot;, widgetEventPrefix:&quot;slide&quot;, options:{animate:!1, distance:0, max:100, min:0, orientation:&quot;horizontal&quot;, range:!1, step:1, value:0, values:null, change:null, slide:null, start:null, stop:null}, _create:function(){this._keySliding=!1, this._mouseSliding=!1, this._animateOff=!0, this._handleIndex=null, this._detectOrientation(), this._mouseInit(), this.element.addClass(&quot;ui-slider ui-slider-&quot;+this.orientation+&quot; ui-widget&quot;+&quot; ui-widget-content&quot;+&quot; ui-corner-all&quot;), this._refresh(), this._setOption(&quot;disabled&quot;, this.options.disabled), this._animateOff=!1}, _refresh:function(){this._createRange(), this._createHandles(), this._setupEvents(), this._refreshValue()}, _createHandles:function(){var e, i, s=this.options, n=this.element.find(&quot;.ui-slider-handle&quot;).addClass(&quot;ui-state-default ui-corner-all&quot;), a=&quot;&lt;a class=&apos;ui-slider-handle ui-state-default ui-corner-all&apos; href=&apos;#&apos;&gt;&lt;/a&gt;&quot;, o=[];for(i=s.values &amp;&amp;s.values.length||1, n.length &gt;i &amp;&amp;(n.slice(i).remove(), n=n.slice(0, i)), e=n.length;i &gt;e;e++) o.push(a);this.handles=n.add(t(o.join(&quot;&quot;)).appendTo(this.element)), this.handle=this.handles.eq(0), this.handles.each(function(e){t(this).data(&quot;ui-slider-handle-index&quot;, e)})}, _createRange:function(){var e=this.options, i=&quot;&quot;;e.range?(e.range===!0 &amp;&amp;(e.values?e.values.length &amp;&amp;2!==e.values.length?e.values=[e.values[0], e.values[0]]:t.isArray(e.values)&amp;&amp;(e.values=e.values.slice(0)):e.values=[this._valueMin(), this._valueMin()]), this.range &amp;&amp;this.range.length?this.range.removeClass(&quot;ui-slider-range-min ui-slider-range-max&quot;).css({left:&quot;&quot;, bottom:&quot;&quot;}):(this.range=t(&quot;&lt;div&gt;&lt;/div&gt;&quot;).appendTo(this.element), i=&quot;ui-slider-range ui-widget-header ui-corner-all&quot;), this.range.addClass(i+(&quot;min&quot;===e.range||&quot;max&quot;===e.range?&quot; ui-slider-range-&quot;+e.range:&quot;&quot;))):(this.range &amp;&amp;this.range.remove(), this.range=null)}, _setupEvents:function(){var t=this.handles.add(this.range).filter(&quot;a&quot;);this._off(t), this._on(t, this._handleEvents), this._hoverable(t), this._focusable(t)}, _destroy:function(){this.handles.remove(), this.range &amp;&amp;this.range.remove(), this.element.removeClass(&quot;ui-slider ui-slider-horizontal ui-slider-vertical ui-widget ui-widget-content ui-corner-all&quot;), this._mouseDestroy()}, _mouseCapture:function(e){var i, s, n, a, o, r, l, h, u=this, c=this.options;return c.disabled?!1:(this.elementSize={width:this.element.outerWidth(), height:this.element.outerHeight()}, this.elementOffset=this.element.offset(), i={x:e.pageX, y:e.pageY}, s=this._normValueFromMouse(i), n=this._valueMax()-this._valueMin()+1, this.handles.each(function(e){var i=Math.abs(s-u.values(e));(n &gt;i||n===i &amp;&amp;(e===u._lastChangedValue||u.values(e)===c.min))&amp;&amp;(n=i, a=t(this), o=e)}), r=this._start(e, o), r===!1?!1:(this._mouseSliding=!0, this._handleIndex=o, a.addClass(&quot;ui-state-active&quot;).focus(), l=a.offset(), h=!t(e.target).parents().addBack().is(&quot;.ui-slider-handle&quot;), this._clickOffset=h?{left:0, top:0}:{left:e.pageX-l.left-a.width()/2, top:e.pageY-l.top-a.height()/2-(parseInt(a.css(&quot;borderTopWidth&quot;), 10)||0)-(parseInt(a.css(&quot;borderBottomWidth&quot;), 10)||0)+(parseInt(a.css(&quot;marginTop&quot;), 10)||0)}, this.handles.hasClass(&quot;ui-state-hover&quot;)||this._slide(e, o, s), this._animateOff=!0,!0))}, _mouseStart:function(){return!0}, _mouseDrag:function(t){var e={x:t.pageX, y:t.pageY}, i=this._normValueFromMouse(e);return this._slide(t, this._handleIndex, i),!1}, _mouseStop:function(t){return this.handles.removeClass(&quot;ui-state-active&quot;), this._mouseSliding=!1, this._stop(t, this._handleIndex), this._change(t, this._handleIndex), this._handleIndex=null, this._clickOffset=null, this._animateOff=!1,!1}, _detectOrientation:function(){this.orientation=&quot;vertical&quot;===this.options.orientation?&quot;vertical&quot;:&quot;horizontal&quot;}, _normValueFromMouse:function(t){var e, i, s, n, a;return&quot;horizontal&quot;===this.orientation?(e=this.elementSize.width, i=t.x-this.elementOffset.left-(this._clickOffset?this._clickOffset.left:0)):(e=this.elementSize.height, i=t.y-this.elementOffset.top-(this._clickOffset?this._clickOffset.top:0)), s=i/e, s &gt;1 &amp;&amp;(s=1), 0 &gt;s &amp;&amp;(s=0),&quot;vertical&quot;===this.orientation &amp;&amp;(s=1-s), n=this._valueMax()-this._valueMin(), a=this._valueMin()+s *n, this._trimAlignValue(a)}, _start:function(t, e){var i={handle:this.handles[e], value:this.value()};return this.options.values &amp;&amp;this.options.values.length &amp;&amp;(i.value=this.values(e), i.values=this.values()), this._trigger(&quot;start&quot;, t, i)}, _slide:function(t, e, i){var s, n, a;this.options.values &amp;&amp;this.options.values.length?(s=this.values(e?0:1), 2===this.options.values.length &amp;&amp;this.options.range===!0 &amp;&amp;(0===e &amp;&amp;i &gt;s||1===e &amp;&amp;s &gt;i)&amp;&amp;(i=s), i!==this.values(e)&amp;&amp;(n=this.values(), n[e]=i, a=this._trigger(&quot;slide&quot;, t,{handle:this.handles[e], value:i, values:n}), s=this.values(e?0:1), a!==!1 &amp;&amp;this.values(e, i))):i!==this.value()&amp;&amp;(a=this._trigger(&quot;slide&quot;, t,{handle:this.handles[e], value:i}), a!==!1 &amp;&amp;this.value(i))}, _stop:function(t, e){var i={handle:this.handles[e], value:this.value()};this.options.values &amp;&amp;this.options.values.length &amp;&amp;(i.value=this.values(e), i.values=this.values()), this._trigger(&quot;stop&quot;, t, i)}, _change:function(t, e){if(!this._keySliding &amp;&amp;!this._mouseSliding){var i={handle:this.handles[e], value:this.value()};this.options.values &amp;&amp;this.options.values.length &amp;&amp;(i.value=this.values(e), i.values=this.values()), this._lastChangedValue=e, this._trigger(&quot;change&quot;, t, i)}}, value:function(t){return arguments.length?(this.options.value=this._trimAlignValue(t), this._refreshValue(), this._change(null, 0), undefined):this._value()}, values:function(e, i){var s, n, a;if(arguments.length &gt;1) return this.options.values[e]=this._trimAlignValue(i), this._refreshValue(), this._change(null, e), undefined;if(!arguments.length) return this._values();if(!t.isArray(arguments[0])) return this.options.values &amp;&amp;this.options.values.length?this._values(e):this.value();for(s=this.options.values, n=arguments[0], a=0;s.length &gt;a;a+=1) s[a]=this._trimAlignValue(n[a]), this._change(null, a);this._refreshValue()}, _setOption:function(e, i){var s, n=0;switch(&quot;range&quot;===e &amp;&amp;this.options.range===!0 &amp;&amp;(&quot;min&quot;===i?(this.options.value=this._values(0), this.options.values=null):&quot;max&quot;===i &amp;&amp;(this.options.value=this._values(this.options.values.length-1), this.options.values=null)), t.isArray(this.options.values)&amp;&amp;(n=this.options.values.length), t.Widget.prototype._setOption.apply(this, arguments), e){case&quot;orientation&quot;:this._detectOrientation(), this.element.removeClass(&quot;ui-slider-horizontal ui-slider-vertical&quot;).addClass(&quot;ui-slider-&quot;+this.orientation), this._refreshValue();break;case&quot;value&quot;:this._animateOff=!0, this._refreshValue(), this._change(null, 0), this._animateOff=!1;break;case&quot;values&quot;:for(this._animateOff=!0, this._refreshValue(), s=0;n &gt;s;s+=1) this._change(null, s);this._animateOff=!1;break;case&quot;min&quot;:case&quot;max&quot;:this._animateOff=!0, this._refreshValue(), this._animateOff=!1;break;case&quot;range&quot;:this._animateOff=!0, this._refresh(), this._animateOff=!1}}, _value:function(){var t=this.options.value;return t=this._trimAlignValue(t)}, _values:function(t){var e, i, s;if(arguments.length) return e=this.options.values[t], e=this._trimAlignValue(e);if(this.options.values &amp;&amp;this.options.values.length){for(i=this.options.values.slice(), s=0;i.length &gt;s;s+=1) i[s]=this._trimAlignValue(i[s]);return i}return[]}, _trimAlignValue:function(t){if(this._valueMin()&gt;=t) return this._valueMin();if(t &gt;=this._valueMax()) return this._valueMax();var e=this.options.step &gt;0?this.options.step:1, i=(t-this._valueMin())%e, s=t-i;return 2 *Math.abs(i)&gt;=e &amp;&amp;(s+=i &gt;0?e:-e), parseFloat(s.toFixed(5))}, _valueMin:function(){return this.options.min}, _valueMax:function(){return this.options.max}, _refreshValue:function(){var e, i, s, n, a, o=this.options.range, r=this.options, l=this, h=this._animateOff?!1:r.animate, u={};this.options.values &amp;&amp;this.options.values.length?this.handles.each(function(s){i=100 *((l.values(s)-l._valueMin())/(l._valueMax()-l._valueMin())), u[&quot;horizontal&quot;===l.orientation?&quot;left&quot;:&quot;bottom&quot;]=i+&quot;%&quot;, t(this).stop(1, 1)[h?&quot;animate&quot;:&quot;css&quot;](u, r.animate), l.options.range===!0 &amp;&amp;(&quot;horizontal&quot;===l.orientation?(0===s &amp;&amp;l.range.stop(1, 1)[h?&quot;animate&quot;:&quot;css&quot;]({left:i+&quot;%&quot;}, r.animate), 1===s &amp;&amp;l.range[h?&quot;animate&quot;:&quot;css&quot;]({width:i-e+&quot;%&quot;},{queue:!1, duration:r.animate})):(0===s &amp;&amp;l.range.stop(1, 1)[h?&quot;animate&quot;:&quot;css&quot;]({bottom:i+&quot;%&quot;}, r.animate), 1===s &amp;&amp;l.range[h?&quot;animate&quot;:&quot;css&quot;]({height:i-e+&quot;%&quot;},{queue:!1, duration:r.animate}))), e=i}):(s=this.value(), n=this._valueMin(), a=this._valueMax(), i=a!==n?100 *((s-n)/(a-n)):0, u[&quot;horizontal&quot;===this.orientation?&quot;left&quot;:&quot;bottom&quot;]=i+&quot;%&quot;, this.handle.stop(1, 1)[h?&quot;animate&quot;:&quot;css&quot;](u, r.animate),&quot;min&quot;===o &amp;&amp;&quot;horizontal&quot;===this.orientation &amp;&amp;this.range.stop(1, 1)[h?&quot;animate&quot;:&quot;css&quot;]({width:i+&quot;%&quot;}, r.animate),&quot;max&quot;===o &amp;&amp;&quot;horizontal&quot;===this.orientation &amp;&amp;this.range[h?&quot;animate&quot;:&quot;css&quot;]({width:100-i+&quot;%&quot;},{queue:!1, duration:r.animate}),&quot;min&quot;===o &amp;&amp;&quot;vertical&quot;===this.orientation &amp;&amp;this.range.stop(1, 1)[h?&quot;animate&quot;:&quot;css&quot;]({height:i+&quot;%&quot;}, r.animate),&quot;max&quot;===o &amp;&amp;&quot;vertical&quot;===this.orientation &amp;&amp;this.range[h?&quot;animate&quot;:&quot;css&quot;]({height:100-i+&quot;%&quot;},{queue:!1, duration:r.animate}))}, _handleEvents:{keydown:function(i){var s, n, a, o, r=t(i.target).data(&quot;ui-slider-handle-index&quot;);switch(i.keyCode){case t.ui.keyCode.HOME:case t.ui.keyCode.END:case t.ui.keyCode.PAGE_UP:case t.ui.keyCode.PAGE_DOWN:case t.ui.keyCode.UP:case t.ui.keyCode.RIGHT:case t.ui.keyCode.DOWN:case t.ui.keyCode.LEFT:if(i.preventDefault(),!this._keySliding &amp;&amp;(this._keySliding=!0, t(i.target).addClass(&quot;ui-state-active&quot;), s=this._start(i, r), s===!1)) return}switch(o=this.options.step, n=a=this.options.values &amp;&amp;this.options.values.length?this.values(r):this.value(), i.keyCode){case t.ui.keyCode.HOME:a=this._valueMin();break;case t.ui.keyCode.END:a=this._valueMax();break;case t.ui.keyCode.PAGE_UP:a=this._trimAlignValue(n+(this._valueMax()-this._valueMin())/e);break;case t.ui.keyCode.PAGE_DOWN:a=this._trimAlignValue(n-(this._valueMax()-this._valueMin())/e);break;case t.ui.keyCode.UP:case t.ui.keyCode.RIGHT:if(n===this._valueMax()) return;a=this._trimAlignValue(n+o);break;case t.ui.keyCode.DOWN:case t.ui.keyCode.LEFT:if(n===this._valueMin()) return;a=this._trimAlignValue(n-o)}this._slide(i, r, a)}, click:function(t){t.preventDefault()}, keyup:function(e){var i=t(e.target).data(&quot;ui-slider-handle-index&quot;);this._keySliding &amp;&amp;(this._keySliding=!1, this._stop(e, i), this._change(e, i), t(e.target).removeClass(&quot;ui-state-active&quot;))}}})})(jQuery):&#160;jquery-ui-1.10.4.custom.min.js'],['../static_2root_2js_2jquery-ui_8custom_8min_8js.html#a175590539c18cdb8be1adc1c2cb681a5',1,'widget(&quot;ui.mouse&quot;,{version:&quot;1.10.3&quot;, options:{cancel:&quot;input,textarea,button,select,option&quot;, distance:1, delay:0}, _mouseInit:function(){var t=this;this.element.bind(&quot;mousedown.&quot;+this.widgetName, function(e){return t._mouseDown(e)}).bind(&quot;click.&quot;+this.widgetName, function(i){return!0===e.data(i.target, t.widgetName+&quot;.preventClickEvent&quot;)?(e.removeData(i.target, t.widgetName+&quot;.preventClickEvent&quot;), i.stopImmediatePropagation(),!1):undefined}), this.started=!1}, _mouseDestroy:function(){this.element.unbind(&quot;.&quot;+this.widgetName), this._mouseMoveDelegate &amp;&amp;e(document).unbind(&quot;mousemove.&quot;+this.widgetName, this._mouseMoveDelegate).unbind(&quot;mouseup.&quot;+this.widgetName, this._mouseUpDelegate)}, _mouseDown:function(i){if(!t){this._mouseStarted &amp;&amp;this._mouseUp(i), this._mouseDownEvent=i;var s=this, n=1===i.which, a=&quot;string&quot;==typeof this.options.cancel &amp;&amp;i.target.nodeName?e(i.target).closest(this.options.cancel).length:!1;return n &amp;&amp;!a &amp;&amp;this._mouseCapture(i)?(this.mouseDelayMet=!this.options.delay, this.mouseDelayMet||(this._mouseDelayTimer=setTimeout(function(){s.mouseDelayMet=!0}, this.options.delay)), this._mouseDistanceMet(i)&amp;&amp;this._mouseDelayMet(i)&amp;&amp;(this._mouseStarted=this._mouseStart(i)!==!1,!this._mouseStarted)?(i.preventDefault(),!0):(!0===e.data(i.target, this.widgetName+&quot;.preventClickEvent&quot;)&amp;&amp;e.removeData(i.target, this.widgetName+&quot;.preventClickEvent&quot;), this._mouseMoveDelegate=function(e){return s._mouseMove(e)}, this._mouseUpDelegate=function(e){return s._mouseUp(e)}, e(document).bind(&quot;mousemove.&quot;+this.widgetName, this._mouseMoveDelegate).bind(&quot;mouseup.&quot;+this.widgetName, this._mouseUpDelegate), i.preventDefault(), t=!0,!0)):!0}}, _mouseMove:function(t){return e.ui.ie &amp;&amp;(!document.documentMode||9 &gt;document.documentMode)&amp;&amp;!t.button?this._mouseUp(t):this._mouseStarted?(this._mouseDrag(t), t.preventDefault()):(this._mouseDistanceMet(t)&amp;&amp;this._mouseDelayMet(t)&amp;&amp;(this._mouseStarted=this._mouseStart(this._mouseDownEvent, t)!==!1, this._mouseStarted?this._mouseDrag(t):this._mouseUp(t)),!this._mouseStarted)}, _mouseUp:function(t){return e(document).unbind(&quot;mousemove.&quot;+this.widgetName, this._mouseMoveDelegate).unbind(&quot;mouseup.&quot;+this.widgetName, this._mouseUpDelegate), this._mouseStarted &amp;&amp;(this._mouseStarted=!1, t.target===this._mouseDownEvent.target &amp;&amp;e.data(t.target, this.widgetName+&quot;.preventClickEvent&quot;,!0), this._mouseStop(t)),!1}, _mouseDistanceMet:function(e){return Math.max(Math.abs(this._mouseDownEvent.pageX-e.pageX), Math.abs(this._mouseDownEvent.pageY-e.pageY))&gt;=this.options.distance}, _mouseDelayMet:function(){return this.mouseDelayMet}, _mouseStart:function(){}, _mouseDrag:function(){}, _mouseStop:function(){}, _mouseCapture:function(){return!0}})})(jQuery):&#160;jquery-ui.custom.min.js']]],
  ['windowname_5fto_5fid',['windowname_to_id',['../_related_object_lookups_8js.html#a60c22114155f281d57bdb3519a80da38',1,'RelatedObjectLookups.js']]],
  ['wt',['wt',['../jquery-1_89_81_8min_8js.html#a62c217633711432c70c8c8189990ba5b',1,'wt(e, t, n, r):&#160;jquery-1.9.1.min.js'],['../jquery_8min_8js.html#a62c217633711432c70c8c8189990ba5b',1,'wt(e, t, n, r):&#160;jquery.min.js']]]
];