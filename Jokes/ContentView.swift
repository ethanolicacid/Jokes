//
//  ContentView.swift
//  Jokes
//
//  Created by Ethan Lim on 2/7/22.
//

import SwiftUI

struct ContentView: View {

    var jokesList = [
    Joke(setup: "My friend had a bakery that caught fire.", punchline: "The bakery is now toast.", explainer: "Toast is a product of toasting bread, but to say that a business is toast also means that the business is done - no more business."),
    Joke(setup: "I only seem to get sick on weekdays.", punchline: "I think I have a weekend immune system.", explainer: "Weakened sounds like weekend. So saying that he has a weekend immune system sounds like he has a weakened immune system that only functions on weekends for some reason"),
    Joke(setup: "Which days of the week are strongest?", punchline: "Saturdays and Sundays, the other days are weekdays.", explainer: "Week sounds like weak, so weekdays sounds like weak days."),
    Joke(setup: "Why couldn't the bicycle stand up by itself?", punchline: "It was too tired", explainer: "A bicycle has 2 wheel tires, so it can be described as two-tired, which sounds similar to the phrase too tired.")
    ]
    @State var showPunchline = false
    @State var showExplainer = false
    @State var currentJoke = 0
    
    @State var isFeedbackPresented = false
    
    @State var isFeedbackResponsePresented = false
    @State var isFeedbackPositive = false
    
    @State var punchlineSize: CGFloat = 0.1
    var body: some View {
        ZStack{
            Color(.systemBackground)
                .onTapGesture {
                    if showPunchline{
                        currentJoke += 1
                        showPunchline = false
                        showExplainer = false
                        isFeedbackPresented = true
                    }
                }
            VStack{
                HStack{
                    Text(jokesList[currentJoke % jokesList.count].setup)
                        .font(.title2)
                        .padding()
                    Spacer()
                    Button{
                        withAnimation{
                            print("Button tapped")
                            showPunchline = true
                        }
                    } label:{
                        Text("Then?")
                            .font(.title2)
                            .foregroundColor(.white)
                            .padding(10)
                            .background(Color(red: 0.2, green: 0.4, blue: 0.9))
                            .cornerRadius(10)
                            .padding(10)
                    }
                    .padding(5)
                }
                .padding(5)
                
                if showPunchline{
                    HStack{
                        Text(jokesList[currentJoke % jokesList.count].punchline)
                            .padding()
                            .scaleEffect(punchlineSize)
                            .onAppear{
                                withAnimation(.easeInOut(duration: 0.5)){
                                    punchlineSize = 1.1
                                }
                            }
                        Spacer()
                        Button{
                            print("User pressed for suicide punchline")
                            showExplainer = true
                        } label:{
                            Text("Huh?")
                                .font(.title3)
                                .foregroundColor(.white)
                                .padding(12)
                                .background(Color(red: 0.2, green: 0.4, blue: 0.9))
                                .cornerRadius(10)
                                .padding(10)
                        }
                        .padding()
                    }
                    if showExplainer{
                    Text(jokesList[currentJoke % jokesList.count].explainer!)
                        .padding()
                        .frame(alignment: .leading)
                    }
            Text("Tap screen for next joke")
                .foregroundColor(Color(red: 0.4, green: 0.4, blue: 0.4))
                }
            }
        }
        .alert(isPresented: $isFeedbackPresented){
            Alert(title: Text("Did you like that joke?"),
                primaryButton: .default(Text("It was amazing")){
                print("User is good")
                isFeedbackPositive = true
                isFeedbackResponsePresented = true
            }, secondaryButton: .default(Text("I need to vomit")){
                print("User is rubbish")
                isFeedbackPositive = false
                isFeedbackResponsePresented = true
                })
        }
        .sheet(isPresented: $isFeedbackResponsePresented){
            FeedbackResponseView(isPositive: isFeedbackPositive)
        }
    }
}
struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
