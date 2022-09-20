$('#calendarFull').fullCalendar({
    header: {
        left: 'prev,next today',
        center: 'title',
        right: 'month,agendaWeek,agendaDay'
    },
    defaultView: 'month',
    editable: true,
    eventSources: [
      {
        events: [
          {
            title: "event3",
            start: "2019-03-09T12:30:00"
          }
        ],
        color: "black", // an option!
        textColor: "yellow" // an option!
      }
    ],
    select: function( start, end, jsEvent, view ) {
        // set values in inputs
        $('#event-modal').find('input[name=evtStart]').val(
            start.format('YYYY-MM-DD HH:mm:ss')
        );
        $('#event-modal').find('input[name=evtEnd]').val(
            end.format('YYYY-MM-DD HH:mm:ss')
        );
        
        // show modal dialog
        $('#event-modal').modal('show');
        
        /*
        bind event submit. Will perform a ajax call in order to save the event to the database.
        When save is successful, close modal dialog and refresh fullcalendar.
        */
        /*
        $("#event-modal").find('form').on('submit', function() {
            $.ajax({
                url: 'yourFileUrl.php',
                data: $("#event-modal").serialize(),
                type: 'post',
                dataType: 'json',
                success: function(response) {
                    // if saved, close modal
                    $("#event-modal").modal('hide');
                    
                    // refetch event source, so event will be showen in calendar
                    $("#calendar").fullCalendar( 'refetchEvents' );
                }
            });
        });*/
    },
    selectHelper: true,
    selectable: true,
    snapDuration: '00:10:00'
});