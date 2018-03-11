
  $(document).ready(function() {

    $('#calendar').fullCalendar({
      height: $(window).height()*0.83,
      header: {
        left: 'prev,next today',
        center: 'title',
        right: 'month,basicWeek,basicDay'
      },
      defaultDate: '2018-03-12',
      navLinks: true,
      editable: true,
      eventLimit: true,
      events: a
    });
      if(calendar) {
  $(window).resize(function() {
    var calHeight = $(window).height()*0.83;
    $('#calendar').fullCalendar('option', 'height', calHeight);
  });
};
  });