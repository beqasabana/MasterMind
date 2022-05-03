var player_form = document.getElementById('player_guess_form')
const start_time = new Date()
var turn_start_time = new Date()
var hint_button = document.getElementById('hint-button')
hint_button.addEventListener('click', display_hint)

setInterval(display_timer, 1000)

player_form.onsubmit = function(e){
    e.preventDefault()
    var form = new FormData(player_form)
    fetch('http://localhost:8000/check', { method : 'POST', body : form })
        .then( response => response.json() )
        .then( data => {
            if (data.status == 0) {
                location.replace('http://localhost:8000/lost')
            }
            else if (data.status == 2) {
                location.replace('http://localhost:8000/victory')
            }
            else {
                var results_div = document.getElementById('results')

                var new_row = document.createElement('div')
                new_row.classList.add('row', 'mt-3')

                var new_result = document.createElement('div')
                new_result.classList.add('col', 'd-flex', 'justify-content-center', 'align-items-center')

                var new_player_input = document.createElement('div')
                new_player_input.classList.add('col', 'd-flex', 'justify-content-center', 'align-items-center')
                
                for (var i = 0; i < data.results.length; i++){
                    // creating color coded code results
                    var color_coded_result = document.createElement('div')
                    color_coded_result.classList.add('result-dot', 'ms-3', 'me-3', data.results[i])
                    new_result.append(color_coded_result)

                    // creating players input for tracking
                    var player_input_single = document.createElement('div')
                    player_input_single.classList.add('result-dot', 'ms-3', 'me-3', 'text-center')
                    var number_guessed = document.createElement('h4')
                    number_guessed.innerText = data.player_input[i]
                    player_input_single.append(number_guessed)
                    new_player_input.append(player_input_single)
                }

                // time spent on turn
                var turn_timer = document.createElement('div')
                turn_timer.classList.add('col', 'text-center')
                var turn_timer_text = document.createElement('h4')
                turn_timer_text.innerText = time_to_string(Date.now() - turn_start_time)
                turn_timer.append(turn_timer_text)
                // reassign turn start time
                turn_start_time = new Date()

                new_row.append(new_result)
                new_row.append(new_player_input)
                new_row.append(turn_timer)
                results_div.prepend(new_row)
                player_form.reset()
            }
        } )
}

function display_timer(){
    let timer = document.getElementById('timer')
    timer.innerText = time_to_string(Date.now() - start_time)

}

// time to string function, takes time in milliseconds and return human readable time string
function time_to_string(time) {
    let hours = time / 3600000
    let hh = Math.floor(hours)

    let minutes = (hours - hh) * 60
    let mm = Math.floor(minutes)

    let seconds = (minutes - mm) * 60
    let ss = Math.floor(seconds)

    let formattedHH = hh.toString().padStart(2, '0')
    let formattedMM = mm.toString().padStart(2, '0')
    let formattedSS = ss.toString().padStart(2, '0')

    return `${formattedHH}:${formattedMM}:${formattedSS}`
}


// function for displaying hint to user
function display_hint(){
    fetch('http://localhost:8000/giveHint')
        .then(response => response.json())
        .then(hint => {
            let hints_container = document.getElementById('hints-container')
            let single_hint = document.createElement('p')
            single_hint.classList.add('m-2')
            single_hint.innerText = '\nHint: ' + hint.hint
            let hint_holder = document.createElement('div')
            hint_holder.classList.add('col')
            hint_holder.append(single_hint)
            hints_container.prepend(hint_holder)
        })
}