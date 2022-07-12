//
//  FeedbackResponseView.swift
//  Jokes
//
//  Created by Ethan Lim on 6/7/22.
//

import SwiftUI

struct FeedbackResponseView: View {
    var body: some View {
        VStack{
            Image("happy")
                .resizable()
                .scaledToFit()
            Text("You are amazing!")
                .font(.title3)
                .padding()
        }
    }
}

struct FeedbackResponseView_Previews: PreviewProvider {
    static var previews: some View {
        FeedbackResponseView()
    }
}
